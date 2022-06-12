<!------------------------------------------------------------------------>
<!------------------------- Templates ------------------------------------>
<!------------------------------------------------------------------------>
<template>
<div>
    <b-form inline id='InputAnualDividendForm' @submit="onSubmit">
        <div class="group">
            <b-form-file 
                v-model="file" 
                class="mt-3" plain
                type="file" 
                @change="handleFileUpload( $event )">
            </b-form-file>
        </div>

        <div class="group">
            <label class="sr-only" :for="Separator" >Separator:</label>
            <b-form-input
                :id="Separator"
                class="form_input"
                v-model='Separator'
                placeholder='Separator type'
            >
            </b-form-input>
        </div>

        <div>
            <div class="RateInput" v-for="Currency in Currencies" :key="Currency.id">
                <label class="sr-only" :for="Currency">{{Currency}}:</label>
                <b-form-input 
                    :id="Currency" 
                    class="form_input CurrencyList"
                    placeholder= "Enter exchange rate">
                </b-form-input>
            </div>
        </div>

        <b-button id="submit-1" type="submit" variant="primary">Add Annual Dividends</b-button>
    </b-form>
</div>
</template>

<!------------------------------------------------------------------------>
<!--------------------------- Scripts ------------------------------------>
<!------------------------------------------------------------------------>
<script>
// imported libraries                     v-model="text" 
import axios from 'axios'; //needed to call flask

export default {
    name:"FormImportAnualDividend",

    data(){
        return{
            //*.csv file with annual dividend data
            file:null,
            Currencies:['EUR','USD','GBP','HKD'],
            Separator:'',
            currencyDict:{},
            csvData:''
        }
    },
    methods:{
        // handel file before sending it to the server (https://serversideup.net/uploading-files-vuejs-axios/)
        handleFileUpload(event ){
            this.file = event.target.files[0];
            
            const reader = new FileReader();
            reader.readAsText(this.file);
            reader.onload = () => {
                this.csvData= reader.result
            };
            reader.onerror = () => {
            };
        },

        async onSubmit(event){
            try{
                event.preventDefault()
                // this.isLoading = true
                const path = 'http://localhost:5000/addAnualDividends'

                // get Exchange rate from Form Inputs to send to server
                var myElements = document.getElementsByClassName("CurrencyList")
                for(var i = 0; i < myElements.length; i++){
                    let myKey = myElements[i].id
                    let myValue = myElements[i].value
                    this.currencyDict[myKey] = myValue // to pass a variable as a key in an objet a [] is needed
                }
       
                // create the array to send to the server
                let postData = [this.currencyDict,  this.csvData, this.Separator]
                let res = await axios.post(path, postData)
                alert(res.data)
            }catch(error){console.log(error)}
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

button{
    margin-top: 20px;
    margin-left: 20px
}

.RateInput{
    display:flex;
    margin-left: 20px;
    margin-top: 20px;
}

.sr-only{
    width: 100px;
    padding-top:5px;
}

.form_input{
    width: 300px;
}
</style>

