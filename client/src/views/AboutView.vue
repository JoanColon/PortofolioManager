<template>
  <div class="about">
    <h1>This is an about page</h1>

    <FormExample/>

  
    <div>

    </div>
  </div>

</template>

<script>
import FormExample from '@/components/FormExample.vue'

export default {
  name: 'AboutView',
  components:{
    FormExample,
  }
  
}
</script>