<template>
  <member v-if="showChatinterface">
    <div>
           <ProfileMain :size="'w-14'" :attributes="roomMemberAvatar" />
<h1>You are chatting with <strong>{{roomMemberName}}</strong></h1>
     </div>
    </member> 
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

}
  
}
</script>