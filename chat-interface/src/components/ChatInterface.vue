<template>
<div>
  <div class="container-sm mt-36">
    <div>
      <SingleMessage
        v-for="{ _id, text, user_name} in messages"
        :key="_id.$oid"
        :name="user_name"
        :sender="user_name=== currentUser"
        :avatar="user_name=== currentUser ? currentUserAvatar : roomMemberAvatar"

      >
        {{ text }}
      </SingleMessage>
    </div>
  </div>
  <div ref="bottom" class="mt-20" />

  <div class="bottom">
    <div class="container-sm">
      <form @submit.prevent="sendMessage">
        <input v-model="message" placeholder="Message"  />
        <n-button class="mt-2" type="info" ghost :disabled="messageEmpty" @click="sendMessage">
          <SendIcon />
        </n-button>
      </form>
    </div>
  </div>
  </div>  
</template>

<script>
import { mapGetters} from 'vuex'
import { mapFields } from 'vuex-map-fields';


import SendIcon from './SendIcon.vue'
import SingleMessage from './SingleMessage.vue'

export default {
  components: { SingleMessage, SendIcon },



  methods: {
    sendMessage (){
      this.$store.dispatch('EMIT_MESSAGE', this.$socket)
    }
  },

  computed: {

    ...mapFields(['message']),

    ...mapGetters([
      'messages',
      'currentUser',
      'currentUserAvatar',
      'roomMemberAvatar',
      'roomMemberName',
      'messageEmpty',

    ]),

  }

}
</script>
