<!------------------------------------------------------------------------>
<!------------------------- Templates ------------------------------------>
<!------------------------------------------------------------------------>
<template>
<div>
  <b-form inline id="NewOrder" @submit="onSubmit">
        <div class="group">
            <label class="sr-only" for="inline-form-input-name">Order type:</label>
            <b-form-select 
                id='select-1'
                class="form_input" 
                :options="['Buy', 'Sell']" 
                required 
                v-model='EnterOrder.OrderType'
            ></b-form-select>
        </div>

        <div class="group">
            <label class="sr-only" for="inline-form-input-name">Order date:</label>
            <b-form-datepicker 
                id="orderDate"
                class="form_input"
                required  
                v-model="EnterOrder.Date" 
            ></b-form-datepicker>
        </div>

        <div class="group">
            <label class="sr-only" for="inline-form-input-name">Ticker:</label>
            <b-form-select
                id='select-2'
                class="form_input"
                :options='tickerList'
                required 
                v-model="EnterOrder.Ticker" 
            ></b-form-select>
        </div>

        <div class="group">
            <label class="sr-only" for="inline-form-input-name">Amount:</label>
            <b-form-input 
            id="input-3"
            class="form_input" 
            placeholder="Enter Amount of shares" 
            required
            v-model='EnterOrder.Amount'
            ></b-form-input>
        </div>        

        <div class="group">
            <label class="sr-only" for="inline-form-input-name">Price:</label>
            <b-form-input 
            id="input-3"
            class="form_input" 
            placeholder="Enter Price" 
            required
            v-model='EnterOrder.Price'
            ></b-form-input>
        </div>

        <b-button id="submitNewOrder" type="submit" variant="primary">Add new order</b-button>
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
    name:"FormNewOrder",

    data(){
        return{
            // Ticker list
            tickerList:[],

            //data for the input form to be send to the ddbb
            EnterOrder:{
                OrderType:'',
                Date:'',
                Ticker:'',
                Amount:'',
                Price:''
            },
        }
    },
    methods:{
        // function to get all tickers from sqlite table and populate the Ticker dropdown in the form
        async getTickers(){
            try{
                const path='http://localhost:5000/getTickers'
                let {data} = await axios.get(path)
                this.tickerList=data.sort()
            } catch(error){console.log(error)}
        },

        // function tu submit the "FormNewOrder" when button is clicked (@submit="onSubmit")
        // sends data to flask, in flask it will store the data in database will return updated data and a text response
        onSubmit(event) {
            event.preventDefault() // to prevent reloading the page once we press submit button
            const path='http://localhost:5000/postNewOrder'
            let postData=this.EnterOrder
            axios.post(path, postData)
            .then((res)=>{alert(JSON.stringify(res.data))})
        },
    },
    created(){
        this.getTickers(); //calls the function getTickers when creating the view
  },
}
</script>

<!------------------------------------------------------------------------>
<!---------------------------- Styles ------------------------------------>
<!------------------------------------------------------------------------>
<style scoped>
.btn_toggle{
    background-color:white;
    border:1px solid white;
    color:black
}

.group{
   margin-top: 20px;
   margin-left: 20px;
   display: flex
}

.sr-only{
    width: 115px;
    padding-top:5px;
}

.form_input{
    width: 300px;
}

button{
    margin-top: 20px;
    margin-left: 20px
}
</style>

