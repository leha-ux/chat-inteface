<template>
<div>
<button  @click="sendMessage" :disabled="messageEmpty" type="text info">send</button>
  </div>
</template>
<script>

import { mapGetters} from 'vuex'

export default {

computed: {
...mapGetters([
  'message',
  'messageEmpty'
]),
}
}
</script>

