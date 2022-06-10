<!------------------------------------------------------------------------>
<!------------------------- Templates ------------------------------------>
<!------------------------------------------------------------------------>
<template>
<div>
  <b-form inline id="NewCompanyForm" @submit="onSubmit">
    <div class="group">
        <label class="sr-only" for="inline-form-input-name">Name:</label>
        <b-form-input
        id="inline-form-input-name"
        class="form_input"
        placeholder="Company name"
        required
        v-model='AddNewCompany.CompanyName'
        ></b-form-input>
    </div>

    <div class="group">
        <label class="sr-only" for="inline-form-input-MyTicker">Ticker:</label>
        <b-form-input
        id="inline-form-input-MyTicker"
        class="form_input"
        placeholder="Ticker to display"
        required
        v-model='AddNewCompany.MyTicker'
        ></b-form-input>
    </div>

    <div class="group">
        <label class="sr-only" for="inline-form-input-SearchTicker">Search Ticker:</label>
        <b-form-input
        id="inline-form-input-SearchTicker"
        class="form_input"
        placeholder="API Ticker, e.g., yahoo finance"
        required
        v-model='AddNewCompany.API_Ticker'
        ></b-form-input>
    </div>

    <div class="group">
        <label class="sr-only" for="inline-form-input-Currency">Currency:</label>
        <b-form-input
        id="inline-form-input-Currency"
        class="form_input"
        placeholder="e.g., EUR, USD, GBP"
        required
        v-model='AddNewCompany.Currency'
        ></b-form-input>
    </div>

    <div class="group">
        <label class="sr-only" for="inline-form-input-Country">Country:</label>
        <b-form-input
        id="inline-form-input-Country"
        class="form_input"
        placeholder="Country"
        required
        v-model='AddNewCompany.Country'
        ></b-form-input>
    </div>

    <div class="group">
        <label class="sr-only" for="inline-form-input-Sector">Sector:</label>
        <b-form-select
        id="inline-form-select-Sector"
        :options="['Basic Materials', 'Consumer Cyclical', 'Consumer Defensive', 'Communication Services', 'Energy', 'ETF', 'Financial Services', 'Healtchare', 'Industrials', 'Real State', 'Technology', 'Utilities']" 
        class="form_input"
        required
        v-model='AddNewCompany.Sector'
        ></b-form-select>
    </div>

    <div class="group">
        <label class="sr-only" for="inline-form-input-SupeSector">Super Sector:</label>
        <b-form-select
        id="inline-form-select-SuperSector"
        :options="['Broad Market', 'Cyclical', 'Defensive', 'Sensitive'  ]" 
        class="form_input"
        required="required"
        v-model='AddNewCompany.Supersector'
        ></b-form-select>
    </div>

    <b-button id="submit-1" type="submit" variant="primary">Add new company</b-button>
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
    name:"FormNewCompany",

    data(){
        return{
            //data for the input form
            AddNewCompany:{
                CompanyName:'',
                MyTicker:'',
                API_Ticker:'',
                Currency:'',
                Country:'',
                Sector:'',
                Supersector:'',
            },
        }
    },
    methods:{
        // function tu submit the "NewCompanyForm" when button is clicked (@submit="onSubmit")
        // sends data to flask, in flask it will store the data in database will return updated data and a text response
        onSubmit(event) {
            event.preventDefault()
            // alert(JSON.stringify(this.AddNewCompany))
            const path='http://localhost:5000/addNewCompany'
            let postData=this.AddNewCompany
            axios.post(path, postData)
            .then((res)=>{alert(JSON.stringify(res.data))})
        },
    }
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

