<template>
  <div class="home">

    <FormNewCompany/>
  
  </div>
</template>

<script>
// import components
import FormNewCompany from '@/components/FormNewCompany.vue' //@ redirects to src folder


export default {
  name: 'HomeView',
  components: {
    FormNewCompany
 
  }
}
</script>
