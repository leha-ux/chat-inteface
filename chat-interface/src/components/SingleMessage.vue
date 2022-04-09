<template>
  <div class="message">
    <span v-if="!sender">{{ name }}</span>
    <div class="flex" :class="sender ? 'flex flex-wrap flex-row-reverse shrink' : ''">
      <ProfileMain :size="'w-14'" :attributes="avatar"/>
      <div class="text w-3/4 h-full mt-4" :class="sender ? 'textSend bg-blue-500' : ' textReceive bg-neutral-300'">
        <slot />
      </div>
    </div>
  </div>
</template>

<script>
/* eslint-disable */
import ProfileMain from './ProfileMain.vue'
export default {
  components: { ProfileMain },
  props: {
    name: { type: String, default: '' },
    sender: { type: Boolean, default: false },
    avatar: {type: Object},

  }
}
</script>

