<!------------------------------------------------------------------------>
<!------------------------- Templates ------------------------------------>
<!------------------------------------------------------------------------>
<template>
<div class="stockanalysis">
  <b-row>
    <div class="BaseCards">
      <BaseCard
      :imageName='portofolioImage'
      :title='PortofolioTitle'
      :data='portofolioValue'
      />

      <BaseCard
      :imageName='dividendImage'
      :title='DividendTitle'
      :data='dividenAmount'
      />
    </div>
  </b-row>

  <b-row> 
    <b-tabs content-class="mt-3">
      <b-tab title="Portofolio Table">
        <!-- Table of current portofolio -->
        <BaseTable
          id="PortofolioTable"
          v-if='!isLoading'
          :MyTableItems='portofolioData'
          :MyTableFields='portofolioFields'
          :RowPerPage=100
        />
      </b-tab>

      <b-tab title="Portofolio Charts">
        <!-- Charts of current portofolio -->
      </b-tab>
    </b-tabs>
  </b-row>
</div>
</template>

<!------------------------------------------------------------------------>
<!--------------------------- Scripts ------------------------------------>
<!------------------------------------------------------------------------>
<script>
// imported libraries
import axios from 'axios'; //needed to call flask

// import components
import BaseTable from '@/components/BaseTable.vue'
import BaseCard from '@/components/BaseCard.vue'


export default {
  name: 'ViewPortofolio',
  components: {
    BaseTable,
    BaseCard,
  },
  data(){
    return{
      // data for Portofolio MarketValue BaseCard
      portofolioImage:'Portofolio.png',
      PortofolioTitle: 'Portofolio Market Value:',
      portofolioValue:'',

      // data for annual dividend BaseCard
      dividendImage:"Dividends.png",
      DividendTitle: 'Annual Expected Dividends:',
      dividenAmount:'',

      // data for the current portofolio table
      portofolioData:[],
      portofolioFields:[
        {key:'Name', sortable:true},
        {key:'Country', sortable:true},
        {key:'Currency', sortable:true},
        {key:'Amount', sortable:true},
        {key:'AveragePrice', sortable:false},
        {key:'CurrentPrice', sortable:false},
        {key:'DividendShare', sortable:false},
        {key:'MarketValue (€)', sortable:true},
        {key:'Dividend (€)', sortable:true},
      ],

      //to prevent that the table is rendered before receiving the data
      isLoading: false, 
    };
  },
  methods:{
    //call to flask to get portofolio data 
    async getPortofolioData(){
      try{
        this.isLoading = true
        const path='http://localhost:5000/getPortofolio'
        let {data} = await axios.get(path)
        this.portofolioData=data[0]
        this.dividenAmount=data[1]
        this.portofolioValue=data[2]
        this.isLoading = false
      } catch(error){console.log(error)}
    },
  },
  created(){
    this.getPortofolioData(); //calls the function getPortofolioData when mounting the view
  }
}
</script>

<!------------------------------------------------------------------------>
<!---------------------------- Styles ------------------------------------>
<!------------------------------------------------------------------------>
<style scoped>
.BaseCards{
  display:flex;
}

.stockanalysis{
  margin-top:15px;
  margin-left: 20px;
}

#OrderForm{
  display:flex;
  max-width:100%;
  justify-content: space-around,
}

#select-1{
  width:200px;
  height:34px;
  margin-left: 10px;
  border:1px solid grey;
}
.form-item{
  margin-right: 20px;
}

#PortofolioTable{
  margin-left:20px;
  margin-right:auto;
  width: 95%;
}

button{
  height:37px;
  width:150px;
  bottom: 0px;
}

#btnNewOrder{
    margin-left:20px;
    width:200px
}

</style>