// ----------------------------------------------------------------------------
// ------------------------ TEMPLATES -----------------------------------------
// ----------------------------------------------------------------------------
<template>
  <div class="stockanalysis">
    <h3>The total value of the portofolio is: {{portofolioValue}}</h3>
    <!-- Portofolio table -->
    <table class="table table-striped caption-top">
      <caption>Current Stocks in Freedom Fund portofolio</caption>
      <thead>
        <th>Name</th>
        <th>Symbol</th>
        <th>Amount</th>
        <th>Current Price</th>
        <th>Market Value</th>
        <th>Weight</th>
      </thead>
      <tbody>
        <tr v-for='item in portofolioData' v-bind:key="item.id">
          <td>{{item.Name}}</td>
          <td>{{item.Symbol}}</td>
          <td>{{item.Amount}}</td>
          <td>{{item.CurrentPrice}}</td>
          <td>{{item.MarketValue}}</td>
          <td>{{item.Weight}}</td>
          <td></td>
        </tr>
      </tbody>
    </table>
  </div>
</template>

// ----------------------------------------------------------------------------
// ------------------------------ SCRIPT --------------------------------------
// ----------------------------------------------------------------------------
<script>
// imported libraries
import axios from 'axios'; //needed to call flask

export default {
  name: 'ViewPortofolio',
  data(){
    return{
      portofolioData:[],
      portofolioValue:10000,
    };
  },
  methods:{
    getPortofolioData(){
      const path = 'http://localhost:5000/getPortofolio'; //path to flask route  
      axios.get(path)
        .then((res) => {
          this.portofolioData = res.data; //portofoliData is the variable (empty list) defined in data section
        })
        .catch((error) => {
          console.error(error);
        });
    }
  },
  mounted(){
    this.getPortofolioData(); //calls the function getPortofolioData when mounting the view
  }
}
</script>

// ----------------------------------------------------------------------------
// ------------------------------ STYLES --------------------------------------
// ----------------------------------------------------------------------------
<style scoped>
.stockanalysis{
  margin-top:15px;
  margin-left: 20px;
}

table{
  margin-top: 10px;
  width: 70%;
}

</style>