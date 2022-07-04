<!------------------------------------------------------------------------>
<!------------------------- Templates ------------------------------------>
<!------------------------------------------------------------------------>
<template>
<div>
<b-form inline id="Benchmark" class="Benchmark" @submit="onSubmit">
    <div class="StyleForm">
        <h5>Selected period of years: <strong>{{SliderRange}}</strong></h5>
        <b-form-input 
            id="SliderRange" 
            type="range"
            v-model="SliderRange"  
            min="1" 
            max="10"
        ></b-form-input>

        <b-form-checkbox-group
            id="Checkbox_Index"
            v-model="selected"
            :options="options"
            value-field="value"
            text-field="text"
            name="SelectedIndex"
        ></b-form-checkbox-group>
    </div>
    <div class="StyleButton">
        <b-button id="submit-1" type="submit" variant="primary">Update</b-button>
    </div>
</b-form>
</div>
</template>

<!------------------------------------------------------------------------>
<!--------------------------- Scripts ------------------------------------>
<!------------------------------------------------------------------------>
<script>
// imported libraries
import axios from 'axios'; //needed to call flask

export default {
    name:"FormBenchmark",

    data(){
        return{
            // Slider range data
            SliderRange:'',

            // Checbox data
            selected: [], // Must be an array reference!
            options: [
            { text: 'S&P500', value: 'SP500' },
            { text: 'Euro Stoxx 50', value: 'STOXX50' },
            { text: 'FTSE100', value: 'UK100' },
            { text: 'IBEX Total Return', value: 'IBEXTR' }
            ]
        }
    },
    methods:{
        async onSubmit(event){
            try{
                event.preventDefault() // to prevent reloading the page once we press submit button (in that case, if missing it redirects to tab 1)
                this.isLoading = true
                const path = 'http://localhost:5000/historicBenchmark'
                let {data} = await axios.get(path)
                console.log(data)
                alert(data)
            }catch(error){console.log(error)}
        },
    }
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
    margin-top: 15px;
    margin-bottom: 15px;
    justify-content: space-between;
}

.form-checkbox{
    margin-right: 15px    
}

</style>