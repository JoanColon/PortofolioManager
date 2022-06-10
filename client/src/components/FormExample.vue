<!------------------------------------------------------------------------>
<!------------------------- Templates ------------------------------------>
<!------------------------------------------------------------------------>
<template>
<div>
  <b-form inline id="TestForm" @submit="getTest">
    <b-button id="submit-1" type="submit" variant="primary">Test API call</b-button>
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
    name:"FormExample",

    data(){
        return{
            //data for the input form
        }
    },
    methods:{
        async getTest(){
            try{
                this.isLoading = true
                const path = 'http://localhost:5000/test'
                let {data} = await axios.get(path)
                console.log(data)
            }catch(error){console.log(error)}
        },
    }
}
</script>

<!------------------------------------------------------------------------>
<!---------------------------- Styles ------------------------------------>
<!------------------------------------------------------------------------>
<style scoped>

</style>

