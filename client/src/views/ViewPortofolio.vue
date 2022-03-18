<!------------------------------------------------------------------------>
<!------------------------- Templates ------------------------------------>
<!------------------------------------------------------------------------>
<template>
  <div class="stockanalysis">
    <h3>The total value of the portofolio is: {{portofolioValue}}</h3>
    <h3 class="mb-5">The total amount of anual expected divideds are: {{dividenAmount}}</h3>

    <!-- Table of current portofolio -->
    <BaseTable
          id="PortofolioTable"
          v-if='!isLoading'
          :small="small" 
          :MyTableItems='portofolioData'
          :MyTableFields='portofolioFields'
          :RowPerPage='RowsPerPage' 
        />
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


export default {
  name: 'ViewPortofolio',
  components: {
    BaseTable
  },
  data(){
    return{
      //data for the total value of the portofolio
      portofolioValue:10000,
      dividenAmount:10000,

      // data for the current portofolio table
      portofolioData:[],
      portofolioFields:[
        {key:'Name', sortable:true},
        {key:'Symbol', sortable:true},
        {key:'Amount', sortable:false},
        {key:'CurrentPrice', sortable:false},
        {key:'MarketValue', sortable:false},
        {key:'Weight', sortable: true}
      ],
      RowsPerPage:100,

      //to prevent that the chart and the table are rendered before receiving the data
      isLoading: false, 
    };
  },
  methods:{
    getPortofolioData(){
      this.isLoading = true
      const path = 'http://localhost:5000/getPortofolio'; //path to flask route  
      axios.get(path)
        .then((res) => {
          this.portofolioData = res.data; //portofoliData is the variable (empty list) defined in data section
          this.isLoading = false
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

<!------------------------------------------------------------------------>
<!---------------------------- Styles ------------------------------------>
<!------------------------------------------------------------------------>
<style scoped>
.stockanalysis{
  margin-top:15px;
  margin-left: 20px;
}

#PortofolioTable{
  margin-left:20px;
  margin-right:auto;
  width: 95%;
}

</style>