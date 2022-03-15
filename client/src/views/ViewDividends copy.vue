// ----------------------------------------------------------------------------
// ------------------------ TEMPLATES -----------------------------------------
// ----------------------------------------------------------------------------
<template>
  <div class="dividends">
    <b-row>
      <BaseBarChart :barChartData='dividendYear'/> 
    </b-row>
    <b-row>
      <table class="table table-striped caption-top">
          <caption>Dividends received per company</caption>
          <thead>
            <th>Ticker</th>
            <th>Amount (€)</th>
          </thead>
          <tbody>
            <tr v-for='item in dividendCompany' v-bind:key="item.id">
              <td>{{item.Tickers}}</td>
              <td>{{item.Amount_euro}}</td>
            </tr>
          </tbody>
        </table>
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

export default {
  name: 'ViewDividends',
  components: {
    BaseBarChart,
  },
  data(){
  return{
    dividendCompany:[],
    dividendYear:[],
  };
  },
  methods:{
    getPortofolioDividendData(){
      const path = 'http://localhost:5000/historicDividends'; //path to flask route  
      axios.get(path)
        .then((res) => {
          this.dividendCompany = res.data[0]; //dividendCompany is the variable (empty list) defined in data() section, gets dividend received per company
          this.dividendYear = res.data[1] //dividendYear is the variable (empty list) defined in data() section, gets dividend received per year
        })
        .catch((error) => {
          console.error(error);
        });
    }
  },
  created(){
    this.getPortofolioDividendData(); //calls the function getPortofolioData when creating the view (before mounting)
  }
}
</script>

// ----------------------------------------------------------------------------
// ------------------------------ STYLES --------------------------------------
// ----------------------------------------------------------------------------
<style scoped>
table{
  margin-top: 10px;
  margin-left: 20px;
  width: 70%;
}
td, th{
  text-align: center;
}


</style>