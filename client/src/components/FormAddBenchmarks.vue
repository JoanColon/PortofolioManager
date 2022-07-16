<!------------------------------------------------------------------------>
<!------------------------- Templates ------------------------------------>
<!------------------------------------------------------------------------>
<template>
<div>
  <b-form inline id="AddBenchmark" @submit="onSubmit">
    <p> Connection to rapidApi and will get annual rate of retur for S&P500, FTSE100, EuroSTOXX50 and IBEX35</p>

    <!-- year -->
    <div class="group">
        <label for="year"  class="sr-only">Year:</label>
        <b-form-input 
            id="year"
            class="form_input"  
            v-model="year" 
            placeholder="Enter year">
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
            year:'',        
        }
    },
    methods:{
        // function tu submit the "FormAddBenchmark" when button is clicked (@submit="onSubmit")
        // sends data to flask, in flask it will store the data in database will return updated data and a text response
        async onSubmit(event) {
            try{                                            
            event.preventDefault() // to prevent reloading the page once we press submit button
            const path='http://localhost:5000/addAnnualBenchmark' 
            let postData=this.year
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

