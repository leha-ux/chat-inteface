<template>
    <van-notify v-model:show="show" type="danger">
  <van-icon name="bell" style="margin-right: 4px;" />
  <span>{{errorMessage}}</span>


</van-notify>

</template>

<script>
/* eslint-disable */
import { watch, ref, computed, getCurrentInstance } from 'vue';
import { useStore } from 'vuex'

export default {



setup(){
    const store = useStore()
    const errorMessage = ref('')
    const show = ref(false);



      watch(()=>store.getters.error, function() {
      errorMessage.value = store.getters.error
      show.value = errorMessage.value!=""  ? true : false
      setTimeout(() => {
        show.value = false;
        store.commit('SET_ERROR', '');
      }, 3000);});



      return {
          show,
          errorMessage,  
      }



}
}
</script>
