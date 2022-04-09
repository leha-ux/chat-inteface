<template>
  <nav>
    <div>
      <h1><strong>Bot</strong> or Not</h1>


      <button v-if="login" @click="signout" class="bg-blue-500 hover:bg-blue-400">
        Sign Out
      </button>
    </div>
  </nav>
  </template>

<script>
  /* eslint-disable */
import { mapGetters} from 'vuex'
import ProfileMain from './ProfileMain.vue'

export default {
    components: {
  ProfileMain
  },
    computed: {
    ...mapGetters([
      'login',
      'roomMemberName',
      'roomMemberAvatar',
      'showChatinterface'
    ]),
  },
methods: {
  signout(){
  this.$store.dispatch('logout', this.$socket)
  this.$router.push('/login')
  }
}
  
}
</script>
