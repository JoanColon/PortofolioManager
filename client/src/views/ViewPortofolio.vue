<!------------------------------------------------------------------------>
<!------------------------- Templates ------------------------------------>
<!------------------------------------------------------------------------>
<template>
<div class="stockanalysis">
  <b-row>
    <!----------------------------------------------------------------------------------->
    <!---------------------------- FIXED CARDS ------------------------------------------>
    <!----------------------------------------------------------------------------------->
    <!--- Cards showing current market value, total dividends/year and  dividend yield -->
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

      <BaseCard
      :imageName='YieldImage'
      :title='YieldTitle'
      :data='YieldValue'
      />
    </div>
  </b-row>

  <b-row> 
    <b-tabs content-class="mt-3">
      <!----------------------------------------------------------------------------------->
      <!---------------------------- TABLE tab -------------------------------------------->
      <!----------------------------------------------------------------------------------->
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

      <!----------------------------------------------------------------------------------->
      <!--------------------------- CHARTS tab -------------------------------------------->
      <!----------------------------------------------------------------------------------->
      <b-tab title="Portofolio Charts">
        <b-row>
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
        </b-row>

        <b-row>
          <div class="chartlayout">
            <BaseChartPie
              v-if='!isLoading' 
              :pieChartData='pieStockData'
              :pieChartLabels='pieStockLabels'
              :MyChartTitle='pieStockTitle'
            />

            <BaseChartPie
              v-if='!isLoading' 
              :pieChartData='pieDividendData'
              :pieChartLabels='pieStockLabels'
              :MyChartTitle='pieDividendTitle'
            />
          </div>
        </b-row>
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
import BaseChartPie from '@/components/BaseChartPie.vue'


export default {
  name: 'ViewPortofolio',
  components: {
    BaseTable,
    BaseCard,
    BaseChartPie,
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

      // data for annual dividend yield BaseCard
      YieldImage:"Yield.png",
      YieldTitle: 'Current Dividend Yield:',
      YieldValue:'',

      // data for the current portofolio table
      portofolioData:[],
      portofolioFields:[
        {key:'Name', sortable:true},
        {key:'Country', sortable:true},
        {key:'Currency', sortable:true},
        {key:'Amount', sortable:false},
        {key:'AveragePrice', sortable:false},
        {key:'CurrentPrice', sortable:false},
        {key:'DividendShare', sortable:false},
        {key:'MarketValue (€)', sortable:true},
        {key:'Dividend (€)', sortable:true},
      ],
    
      // data for populating the initial stock chart 
      pieStockData:[],
      pieStockLabels:[],
      pieStockTitle:'Stock % distribution',

      // data for populating the initial dividend chart, labels are the same for both pie charts (only defined above)
      pieDividendData:[],
      pieDividendTitle:'Dividend % distribution',

      //data for the radiobuttons
      selected:'MyTicker', // Initially shows the radio button MyTicker as selected

      RadioOptions:[ // data for populating the radio buttons (BaseRadioBtn) in Portofolio Charts tab 
        {text:'Stock', value:'MyTicker'},
        {text:'Country', value:'Country'},
        {text:'Currency', value:'Currency'},
        {text:'Sector', value:'Sector'},
        {text:'Super Sector', value:'SuperSector'},
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
        this.YieldValue=data[3]
        this.pieStockLabels=data[4]
        this.pieStockData=data[5]
        this.pieDividendData=data[6]
        this.isLoading = false
      } catch(error){console.log(error)}
    },

    // update pie charts according to radiobutton selection
    async onChange() {
      try{
        this.isLoading = true
        let postData={data: this.selected} //data to post must be an object (dictionary)
        const path='http://localhost:5000/PortolioCharts'
        let response= await axios.post(path, postData)
        this.pieStockLabels=response.data[0]
        this.pieStockData=response.data[1]
        this.pieDividendData=response.data[2]
        this.isLoading = false
      } catch(error){console.log(error)}
    },
  },
  created(){
    this.getPortofolioData(); //calls the function getPortofolioData when mounting the view
  },
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

#PortofolioTable{
  margin-left:20px;
  margin-right:auto;
  width: 95%;
}

.chartlayout{
  display:flex
}

</style>