<!------------------------------------------------------------------------>
<!------------------------- Templates ------------------------------------>
<!------------------------------------------------------------------------>
<template>
<div>
  <b-form inline id="UpdateDividends" @submit="onSubmit">
    <p>Update the dividends value, get values from yahoo finance API</p>
    <b-button id="SubmitUpdateDividends" type="submit" variant="primary">Update Dividends</b-button>
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
    name:"FormUpdateDividends",

    data(){
        return{
            nessage: ''
        }
    },
    methods:{
        async onSubmit(event) {
            try{
            event.preventDefault() // to prevent reloading the page once we press submit button
            alert('Starting connection with Rapid Api - Yahoo Financne')
            const path='http://localhost:5000/updateDividends'
            let {data} = await axios.get(path)
            this.message=data
            alert(this.message)
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

