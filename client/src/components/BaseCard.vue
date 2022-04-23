<!------------------------------------------------------------------------>
<!------------------------- Templates ------------------------------------>
<!------------------------------------------------------------------------>
<template>
<div>
  <b-card no-body class="overflow-hidden" style="card">
    <b-row no-gutters>
      <b-col>
        <b-card-img 
            :src="require('@/assets/' + imageName + '')" 
            alt="Image" 
            class="carc-img rounded-0">
        </b-card-img>
      </b-col>
      <b-col>
        <b-card-body :title="title">
          <b-card-text >
            <h4 class="card-text">{{data}}</h4>
          </b-card-text>
        </b-card-body>
      </b-col>
    </b-row>
  </b-card>
</div>
</template>

<!------------------------------------------------------------------------>
<!--------------------------- Scripts ------------------------------------>
<!------------------------------------------------------------------------>
<script>
export default {
    name:'BaseCard',
    props:['title', 'data','imageName'],
}
</script>

<!------------------------------------------------------------------------>
<!---------------------------- Styles ------------------------------------>
<!------------------------------------------------------------------------>
<style scoped>
.card{
    margin-right: 25px;
    margin-bottom: 25px;
    min-width: 475px;
    min-height:115px;
    box-shadow: 5px 5px #888888;
}

.card-img{
    height:100px;
    width:100px;
}

.card-body{
    white-space: nowrap /* makes teh text to fit in one line*/
}

.card-text{
    font-weight: bold;
}

</style>