<!------------------------------------------------------------------------>
<!------------------------- Templates ------------------------------------>
<!------------------------------------------------------------------------>
<template>
  <div>
    <b-row>
        <b-form-input 
            v-model="filter" 
            type="search" 
            id="filterInput" 
            placeholder="Type to Search">
        </b-form-input>

        <b-table 
            id="my-table"
            striped hover 
            class='text-center'  
            :items="items"
            :filter="filter" 
            :fields="fields"
            :per-page="perPage"
            :current-page="currentPage"
      
        ></b-table>

        <b-pagination
            v-model="currentPage"
            :total-rows="rows"
            :per-page="perPage"
            aria-controls="my-table">   
        </b-pagination>
    </b-row>
  </div>
</template>

<!------------------------------------------------------------------------>
<!--------------------------- Scripts ------------------------------------>
<!------------------------------------------------------------------------>
<script>
  export default {
    name:'BaseTable',

    data() {
      return {
        perPage: this.RowPerPage,
        currentPage: 1,
        filter: "",
        items: this.MyTableItems,
        fields: this.MyTableFields
      }
    },

    computed: {
        // detemine the number of pages for the table pagination
        rows() {
            return this.items.length
        }
    },

    props: ['MyTableItems','MyTableFields','RowPerPage'] //imported data from fahter component/view
  }
</script>

<!------------------------------------------------------------------------>
<!---------------------------- Styles ------------------------------------>
<!------------------------------------------------------------------------>
<style scoped>

#filterInput{
  width: 200px;
}
</style>