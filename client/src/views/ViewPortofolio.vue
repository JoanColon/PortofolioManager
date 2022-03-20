<!------------------------------------------------------------------------>
<!------------------------- Templates ------------------------------------>
<!------------------------------------------------------------------------>
<template>
  <div class="stockanalysis">
    <b-row class="mb-3">
      <h3>The total value of the portofolio is: {{portofolioValue}} €</h3>
      <h3>The total amount of anual expected divideds is: {{dividenAmount}} €/year</h3>
    </b-row>

    <!-- Enter new order form -->
    <b-row class="mb-3">
      <b-button v-b-toggle.collapse-1 variant="outline-primary" id="btnNewOrder">Enter a new order</b-button>
      <b-collapse id="collapse-1" class="mt-2">
        <b-form id="OrderForm" @submit="onSubmit">
            <b-form-group id="input-group-1" label="" label-for="select-1" class="form-item">
              <b-form-select 
                id='select-1' 
                :options="['Buy', 'Sell']" 
                required 
                v-model='EnterAction.ActionType'>
              </b-form-select>
            </b-form-group>

            <b-form-group id="input-group-2" label="" label-for="input-2" class="form-item">
              <b-form-input 
                id="input-2" 
                placeholder="Enter ticker" 
                required
                v-model='EnterAction.Ticker'>
              </b-form-input>
            </b-form-group>

            <b-form-group id="input-group-3" label="" label-for="input-3" class="form-item">
              <b-form-input 
                id="input-3" 
                placeholder="Enter Price" 
                required
                v-model='EnterAction.Price'>
              </b-form-input>
            </b-form-group>

            <b-form-gorup id="submit-group-1" class="form-item">
              <b-button id="submit-1" type="submit" variant="primary">Enter Action</b-button>
            </b-form-gorup>
        </b-form>
      </b-collapse>
    </b-row>

    <!-- Table of current portofolio -->
    <b-row> 
      <BaseTable
            id="PortofolioTable"
            v-if='!isLoading'
            :small="small" 
            :MyTableItems='portofolioData'
            :MyTableFields='portofolioFields'
            :RowPerPage=100
          />
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

      //data for the input form
      EnterAction:{
        ActionType:'',
        Ticker:'',
        Price:''
      },

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

      //to prevent that the chart and the table are rendered before receiving the data
      isLoading: false, 
    };
  },
  methods:{
    //call to flask to get portofolio data 
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
    },

    // function tu submit the "Enter New Order" form when buuton is clicke (@submit="onSubmit")
    // sends data to flask, in flask it will store the data in database will return updated data 
    onSubmit(event) {
        event.preventDefault()
        alert(JSON.stringify(this.EnterAction))
    },
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