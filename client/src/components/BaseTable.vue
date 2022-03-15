<template>
  <div>
    <b-row>
        <!-- <b-form-input 
            v-model="filter" 
            type="search" 
            id="filterInput" 
            placeholder="Type to Search">
        </b-form-input> -->
        <b-table 
            id="my-table"
            striped hover
            class='text-center'  
            :items="items" 
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

<script>
  export default {
    name:'BaseTable',
    data() {
      return {
        perPage: 10,
        currentPage: 1,
        // filter: "",
        items: this.MyTableItems,
        fields: this.MyTableFields
      }
    },
    computed: {
        rows() {
            return this.items.length
        }
    },
    props: ['MyTableItems','MyTableFields']
  }
</script>

<style scoped>
td, th{
  text-align: center;
}
</style>