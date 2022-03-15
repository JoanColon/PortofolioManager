// ----------------------------------------------------------------------------
// ------------------------ TEMPLATES -----------------------------------------
// ----------------------------------------------------------------------------
<template>
  <div class="dividends">
    <!-- Chart of total dividend per year -->
    <b-row>
      <BaseBarChart 
        v-if='!isLoading' 
        :barChartData='dividendYear'  
      />
    </b-row>

    <!-- Table of total diviend per company -->
    <b-row>
      <BaseTable
        id="DividendTable" 
        v-if='!isLoading' 
        :MyTableItems='dividendCompany' 
        :MyTableFields='dividendCompanyFields'
      />
    </b-row>
  </div>
</template>

// ----------------------------------------------------------------------------
// ------------------------------ SCRIPT --------------------------------------
// ----------------------------------------------------------------------------
<script>
import axios from 'axios';

// import components
import BaseBarChart from '@/components/BaseBarChart.vue' //@ redirects to src folder
import BaseTable from '@/components/BaseTable.vue' 

export default {
  name: 'ViewDividends',
  components: {
    BaseBarChart,
    BaseTable
  },
  data(){
    return{
      // data for the bar chart
      dividendYear:[], //dividends received per year
    
      // data for the dividend table
      dividendCompany: [], //dividend received by company
      dividendCompanyFields:[
        {key:'Tickers', sortable: true },
        {key:'Amount_euro', sortable: true, label:'Amount (€)' },
        ],
        
      isLoading: false, //to prevent that the chart and the table are rendered before receiving the data
    };
  },
  methods:{
    //call to flack to get dividend data (per year and per company) 
    getPortofolioDividendData(){
      this.isLoading = true
      const path = 'http://localhost:5000/historicDividends'; //path to flask route  
      axios.get(path)
        .then((res) => {
          this.dividendCompany = res.data[0]; //dividendCompany is the variable (empty list) defined in data() section, gets dividend received per company
          this.dividendYear = res.data[1] //dividendYear is the variable (empty list) defined in data() section, gets dividend received per year
          this.isLoading = false
        })
        .catch((error) => {
          console.error(error);
        });
    }
  },
  mounted(){
    this.getPortofolioDividendData(); //calls the function getPortofolioData when mounting the view
  },
}
</script>

// ----------------------------------------------------------------------------
// ------------------------------ STYLES --------------------------------------
// ----------------------------------------------------------------------------
<style scoped>
#DividendTable{
    margin-left: 25px;
    width:50%;
}
</style>