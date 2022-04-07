<!------------------------------------------------------------------------>
<!------------------------- Templates ------------------------------------>
<!------------------------------------------------------------------------>
<template>
<div>
<b-button v-b-toggle.FormUpdatePortofolio class="btn_toggle"><b-icon icon="arrow-down-circle-fill"></b-icon> Update Portofolio</b-button>
<b-collapse id="FormUpdatePortofolio" class="mt-2">
  <b-form inline id="UpdatePortofolio" @submit="onSubmit">
    <b-button id="SubmitUpdatePortofolio" type="submit" variant="primary">Update Portofolio</b-button>
  </b-form>
</b-collapse>
<hr>
</div>
</template>

<!------------------------------------------------------------------------>
<!--------------------------- Scripts ------------------------------------>
<!------------------------------------------------------------------------>
<script>
// imported libraries
import axios from 'axios'; //needed to call flask

export default {
    name:"FormUpdatePortofolio",

    data(){
        return{
            nessage: ''
        }
    },
    methods:{
        async onSubmit(event) {
            try{
            event.preventDefault()
            const path='http://localhost:5000/updatePortoflio'
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

