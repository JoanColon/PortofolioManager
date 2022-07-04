<!------------------------------------------------------------------------>
<!------------------------- Templates ------------------------------------>
<!------------------------------------------------------------------------>
<template>
<div>
  <b-form inline id="NewOrder" @submit="onSubmit">
    <p>Add the CAGR and the dividend rate in percentage &#40;without the % symbol&#41;</p>
    <!-- year -->
    <div class="group">
        <label for="year"  class="sr-only">Year:</label>
        <b-form-input 
            id="year"
            class="form_input"  
            v-model="Benchmark_dict.year" 
            placeholder="Enter year">
        </b-form-input>
    </div>

    <!-- to use v-model with nested objects, if is needed to put the v-if, if not, vue returns undified for the nested property -->

    <!-- S&P500 -->
    <div class="group">
        <label for="SP500"  class="sr-only">S&amp;P500:</label>
        <b-form-input 
            id="SP500"
            class="form_input"
            v-if="Benchmark_dict.FinancialData.sp500"    
            v-model="Benchmark_dict.FinancialData.sp500.cagr" 
            placeholder="SP500 CAGR">
        </b-form-input>
        <b-form-input 
            id="SP500_dividend"
            class="form_input"
            v-if="Benchmark_dict.FinancialData.sp500"   
            v-model="Benchmark_dict.FinancialData.sp500.dividend" 
            placeholder="SP500 dividend">
        </b-form-input>
    </div>

    <!-- FTSE100 -->
    <div class="group">
        <label for="FTSE100"  class="sr-only">FTSE100:</label>
        <b-form-input 
            id="FTSE100"
            class="form_input"
            v-if="Benchmark_dict.FinancialData.ftse100"   
            v-model="Benchmark_dict.FinancialData.ftse100.cagr" 
            placeholder="FTSE100 CAGR">
        </b-form-input>
        <b-form-input 
            id="FTSE100_dividend"
            class="form_input" 
            v-if="Benchmark_dict.FinancialData.ftse100"    
            v-model="Benchmark_dict.FinancialData.ftse100.dividend" 
            placeholder="FTSE100 dividend">
        </b-form-input>
    </div>

    <!-- Eurostoxx 50 -->
    <div class="group">
        <label for="EuroStoxx50"  class="sr-only">Euro Stoxx 50:</label>
        <b-form-input 
            id="EuroStoxx50"
            class="form_input"
            v-if="Benchmark_dict.FinancialData.stoxx50"    
            v-model="Benchmark_dict.FinancialData.stoxx50.cagr" 
            placeholder="EuroStoxx50 CAGR">
        </b-form-input>
        <b-form-input 
            id="EuroStoxx50_dividend"
            class="form_input"
            v-if="Benchmark_dict.FinancialData.stoxx50"     
            v-model="Benchmark_dict.FinancialData.stoxx50.dividend" 
            placeholder="EuroStoxx50 dividend">
        </b-form-input>
    </div>

    <!-- IBEX35 TR -->
    <div class="group">
        <label for="IBEX35_TR"  class="sr-only">IBEX 35 TR:</label>
        <b-form-input 
            id="IBEX35_TR"
            class="form_input"
            v-if="Benchmark_dict.FinancialData.Ibex35TR"     
            v-model="Benchmark_dict.FinancialData.Ibex35TR.cagr" 
            placeholder="IBEX35 TR CAGR">
        </b-form-input>
        <b-form-input 
            id="IBEX35_TR_dividend"
            class="form_input"
            v-if="Benchmark_dict.FinancialData.Ibex35TR"      
            v-model="Benchmark_dict.FinancialData.Ibex35TR.dividend" 
            placeholder="IBEX35 TR dividend">
        </b-form-input>
    </div>

    <!-- submit button -->
    <b-button id="submitNewOrder" type="submit" variant="primary">Add new annual benchmark</b-button>
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
    name:"FormAddBenchmarks",

    data(){
        return{
            Benchmark_dict:{
                year:'',
                FinancialData:{
                    sp500:{
                        cagr:'',
                        dividend:'',
                    },
                    stoxx50:{
                        cagr:'',
                        dividend:'',
                    },
                    ftse100:{
                        cagr:'',
                        dividend:'',
                    },
                    Ibex35TR:{
                        cagr:'',
                        dividend:'',
                    }
                }
            }
        }
    },
    methods:{
        // function tu submit the "FormAddBenchmark" when button is clicked (@submit="onSubmit")
        // sends data to flask, in flask it will store the data in database will return updated data and a text response
        async onSubmit(event) {
            try{                                            
            event.preventDefault() // to prevent reloading the page once we press submit button
            const path='http://localhost:5000/addAnnualBenchmark' 
            let postData=this.Benchmark_dict
            let {data} = await axios.post(path, postData)
            alert(data)
            } catch(error){console.log(error)}     
        },
    },
}
</script>

<!------------------------------------------------------------------------>
<!---------------------------- Styles ------------------------------------>
<!------------------------------------------------------------------------>
<style scoped>
.group{
   margin-top: 20px;
   margin-left: 10px;
   display: flex
}

.sr-only{
    width: 115px;
    padding-top:5px;
}

.form_input{
    width: 165px;
    margin-right: 10px
}

button{
    margin-top: 20px;
    width:50%;
}

</style>

