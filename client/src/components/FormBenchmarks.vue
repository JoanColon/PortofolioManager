<!------------------------------------------------------------------------>
<!------------------------- Templates ------------------------------------>
<!------------------------------------------------------------------------>
<template>
<div>
<b-row>
    <b-col>
        <b-row>
            <BaseChartLineMultiple
                id='ChartLines'
                v-if='!isLoading'
                :MyChartTitle='BenchmarkChartTitle' 
                :lineChartData='BenchmarkChartData' 
                :yaxisTitle='Benchmark_yaxisTitle'
                :xaxisTitle='Benchmark_xaxisTitle' 
            />
        </b-row>

        <b-row>
            <b-form inline id="Benchmark" class="Benchmark" @submit="onSubmit">
                <div class="StyleForm">
                    <b-form-checkbox-group
                        id="Checkbox_Index"
                        v-model="selected"
                        :options="options"
                        value-field="value"
                        text-field="text"
                        name="SelectedIndex"
                    ></b-form-checkbox-group>

                    <h5>Selected period of years: <strong>{{SliderRange}}</strong></h5>
                    <b-form-input 
                        id="SliderRange" 
                        type="range"
                        v-model="SliderRange"  
                        min="1" 
                        max="25"
                    ></b-form-input>
                </div>

                <div class="StyleButton">
                    <b-button id="submit-1" type="submit" variant="primary">Update</b-button>
                </div>
            </b-form>
        </b-row>
    </b-col>

    <b-col>
        <h3>Benchmark key data</h3>
        <BaseTableStatic
            id="BenchmarkTable"
            class='Table' 
            v-if='!isLoading' 
            :MyTableItems='BenchmarkTableData' 
            :MyTableFields='BenchmarkTableFields'
        />
    </b-col>
</b-row>
</div>
</template>

<!------------------------------------------------------------------------>
<!--------------------------- Scripts ------------------------------------>
<!------------------------------------------------------------------------>
<script>
// imported libraries
import axios from 'axios'; //needed to call flask

import BaseChartLineMultiple from '@/components/BaseChartLineMultiple.vue'
import BaseTableStatic from '@/components/BaseTableStatic.vue'

export default {
    name:"FormBenchmark",
    components:{
        BaseChartLineMultiple,
        BaseTableStatic
    },

    data(){
        return{
            // Slider range data
            SliderRange:'10',

            // Checbox data
            selected: ['Portofolio'], // Must be an array reference!
            options: [
            { text: 'Portofolio', value: 'Portofolio' },
            { text: 'S&P500', value: 'sp500' },
            { text: 'Euro Stoxx 50', value: 'stoxx50' },
            { text: 'FTSE100', value: 'ftse100' },
            { text: 'IBEX Total Return', value: 'Ibex35TR' }
            ],

            // data for the benchmark multi line chart
            BenchmarkChartTitle:'Portofolio perfomance vs Benchmark Index',
            BenchmarkChartData:[], 
            Benchmark_yaxisTitle:'Euros (€)',
            Benchmark_xaxisTitle:'Year',

            // data for the benchmark table
            BenchmarkTableData:[],
            BenchmarkTableFields:[
                {key:'BenchmarkIndex', sortable: false, label:'Benchmark Index'},
                {key:'BenchmarkCAGR', sortable: false, label:'Benchmark CAGR (%)'},
                {key:'Value', sortable: false, label:'Value (€)'},
            ],

            //to prevent that the chart and the table are rendered before receiving the data
            isLoading: false, 
        }
    },
    methods:{
        async getPortofolioBenchmark(){
            this.isLoading = true
            const path = 'http://localhost:5000/historicBenchmark'

            let postData = [this.SliderRange, this.selected]
            let {data} = await axios.post(path, postData)
            let chartData = data[0]
            let keyData = data[1]
                   
            this.BenchmarkChartData = []
            for (let i = 0; i < chartData.length; i++) {
                let keyObject = Object.keys(chartData[i])
                let xAxis = chartData[i][keyObject[0]]['xAxis']
                let yAxis = chartData[i][keyObject[0]]['yAxis']
                let traceData = {
                    x: xAxis,
                    y: yAxis,
                    name: keyObject[0],
                    type: "scatter"
                }

                this.BenchmarkChartData.push(traceData)
            }

                this.BenchmarkTableData = []
                for (let i = 0; i < keyData.length; i++){
                    let keyObject = Object.keys(keyData[i])
                    let newKeyData ={
                        'BenchmarkIndex': keyObject[0],
                        'BenchmarkCAGR': keyData[i][keyObject[0]]['CAGR'],
                        'Value': keyData[i][keyObject[0]]['final Value'],
                    }

                    this.BenchmarkTableData.push(newKeyData)
                }
            
            this.isLoading = false
        },

        async onSubmit(event){
            try{
                event.preventDefault() // to prevent reloading the page once we press submit button (in that case, if missing it redirects to tab 1)
                this.isLoading = true
                const path = 'http://localhost:5000/historicBenchmark'
                let postData = [this.SliderRange, this.selected]
                let {data} = await axios.post(path, postData)

                let chartData = data[0]
                let keyData = data[1]
                
                this.BenchmarkChartData = []
                for (let i = 0; i < chartData.length; i++) {
                    let keyObject = Object.keys(chartData[i])
                    let xAxis = chartData[i][keyObject[0]]['xAxis']
                    let yAxis = chartData[i][keyObject[0]]['yAxis']
                    let traceData = {
                        x: xAxis,
                        y: yAxis,
                        name: keyObject[0],
                        type: "scatter"
                    }

                    this.BenchmarkChartData.push(traceData)
                }

                this.BenchmarkTableData = []
                for (let i = 0; i < keyData.length; i++){
                    let keyObject = Object.keys(keyData[i])
                    console.log(keyObject)
                    let newKeyData ={
                        'BenchmarkIndex': keyObject[0],
                        'BenchmarkCAGR': keyData[i][keyObject[0]]['CAGR'],
                        'Value': keyData[i][keyObject[0]]['final Value'],
                    }

                    this.BenchmarkTableData.push(newKeyData)
                }
                
                this.isLoading = false

            }catch(error){console.log(error)}
        },
    },
    mounted(){
        this.getPortofolioBenchmark();
  },
}
</script>

<!------------------------------------------------------------------------>
<!---------------------------- Styles ------------------------------------>
<!------------------------------------------------------------------------>
<style scoped>
.Benchmark{
    display:flex;
    width:700px;
    margin-top:20px;
    margin-left:25px;
}

.StyleButton{
    margin-left:25px;
    margin-top:20px;
}

#SliderRange{
  width: 650px;
}

#Checkbox_Index{
    display: flex;
    margin-top: 0px;
    margin-bottom: 20px;
    justify-content: space-between;
}

.form-checkbox{
    margin-right: 15px    
}

.Table{
  width:75%;
  margin-left:auto;
  margin-right: auto;
}

h3{
  margin-top:25px;
  margin-bottom:25px;
  text-align: center;
}
</style>