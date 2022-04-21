<!------------------------------------------------------------------------>
<!------------------------- Templates ------------------------------------>
<!------------------------------------------------------------------------>
<template>
<div>
    <b-form-group :label="RadioGroupLabel" v-slot="{ ariaDescribedby }">
      <b-form-radio-group
        v-model="selected"
        :options="options"
        :aria-describedby="ariaDescribedby"
        name="plain-inline"
        plain
      ></b-form-radio-group>
    </b-form-group>
    {{selected}}
</div>
</template>

<!------------------------------------------------------------------------>
<!--------------------------- Scripts ------------------------------------>
<!------------------------------------------------------------------------>
<script>
export default {
    name:'BaseRadioBtn',

    props:['options','RadioSelection','RadioGroupLabel'],

    data(){
        return{
            selected: this.RadioSelection,
        }
    },
}
</script>

<!------------------------------------------------------------------------>
<!---------------------------- Styles ------------------------------------>
<!------------------------------------------------------------------------>
<style scoped>

</style>