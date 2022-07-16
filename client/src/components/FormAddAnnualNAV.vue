<!------------------------------------------------------------------------>
<!------------------------- Templates ------------------------------------>
<!------------------------------------------------------------------------>
<template>
<div>
  <b-form inline id="AddAnnualNAV" @submit="onSubmit">
        <div class="group">
            <label class="sr-only" for="inline-form-input-name">Year:</label>
            <b-form-input
            id="Year"
            class="form_input"
            placeholder="Year"
            required
            v-model='AnnualNavData.Year'
            ></b-form-input>
        </div>

        <div class="group">
            <label class="sr-only" for="inline-form-input-name">Deposit:</label>
            <b-form-input
            id="Deposit"
            class="form_input"
            placeholder="Total Annual Deposits (€)"
            required
            v-model='AnnualNavData.Deposit'
            ></b-form-input>
        </div>

        <div class="group">
            <label class="sr-only" for="inline-form-input-name">Withdraw:</label>
            <b-form-input
            id="Withdraw"
            class="form_input"
            placeholder="Total Annual Withdraw (€)"
            required
            v-model='AnnualNavData.Withdraw'
            ></b-form-input>
        </div>

        <div class="group">
            <label class="sr-only" for="inline-form-input-name">Portofolio Value:</label>
            <b-form-input
            id="PortofolioValue"
            class="form_input"
            placeholder="Portofolio Value at 31th December (€)"
            required
            v-model='AnnualNavData.PortofolioValue'
            ></b-form-input>
        </div>

        <b-button id="submitNewOrder" type="submit" variant="primary">Add Annual NAV</b-button>
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
    name:"FormAddAnnualNAV",

    data(){
        return{
            AnnualNavData:{
                Year: '',
                Deposit: '',
                Withdraw: '',
                PortofolioValue: ''
            }
        }
    },
    methods:{
        // function to get all tickers from sqlite table and populate the Ticker dropdown in the form
        async onSubmit(){
            try{
                const path='http://localhost:5000/AddAnnualNAV'
                let postData = this.AnnualNavData
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

