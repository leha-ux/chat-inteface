<template>
<van-loading v-if="showWait" class= "flex justify-center items-center h-screen z-50" size="100px" vertical>Give us a second. We are matching you with another player...</van-loading>

<van-overlay :show="showWait" />


</template>

<script>
/* eslint-disable */
import { watch, ref, computed, getCurrentInstance } from 'vue';
import { useStore } from 'vuex'

export default {

setup(){
    const store = useStore()
    const showWait =  computed(() => store.getters.showWait);

      return {
          showWait,
      }
}
}
</script>
