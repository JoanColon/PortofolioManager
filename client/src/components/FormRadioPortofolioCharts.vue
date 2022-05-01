<!------------------------------------------------------------------------>
<!------------------------- Templates ------------------------------------>
<!------------------------------------------------------------------------>
<template>
<div>
    <b-form-group label='Choose an option to change the chart:' v-slot="{ ariaDescribedby }">
      <b-form-radio-group
        @change="onChange()"
        v-model="selected"
        :options="RadioOptions"
        :aria-describedby="ariaDescribedby"
        name="plain-inline"
        plain
      ></b-form-radio-group>
    </b-form-group>
    {{selected}}
</div>
</template>

<!------------------------------------------------------------------------>
<!--------------------------- Scripts ------------------------------------>
<!------------------------------------------------------------------------>
<script>
// imported libraries
import axios from 'axios'; //needed to call flask

export default {
  name:'FormRadioPortofolioCharts',

  data(){
    return{
      // Initially shows the radio button MyTicker as selected
      selected:'MyTicker',

      // data for populating the radio buttons (BaseRadioBtn) in Portofolio Charts tab 
      RadioOptions:[
        {text:'Stock', value:'MyTicker'},
        {text:'Country', value:'Country'},
        {text:'Currency', value:'Currency'},
        {text:'Sector', value:'Sector'},
        {text:'Super Sector', value:'SuperSector'},
      ],
    }
  },
  methods:{
    async onChange() {
      try{
        let postData={data: this.selected} //data to post must be an object (dictionary)
        const path='http://localhost:5000/PortolioCharts'
        let response= await axios.post(path, postData)
        alert(JSON.stringify(response.data))
      } catch(error){console.log(error)}
    },
  }
}
</script>

<!------------------------------------------------------------------------>
<!---------------------------- Styles ------------------------------------>
<!------------------------------------------------------------------------>
<style scoped>

</style>