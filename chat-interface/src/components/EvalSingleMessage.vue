
<template>
  <div class="message">
    <div class="flex" :class="sender ? 'flex flex-wrap flex-row-reverse shrink' : ''">
      <button type="radio" @click="greet"  :class="computedCSS(sender, selectedMessage)">
        <slot />
      </button>
    </div>
  </div>
</template>
<script>

export default {
  data () {
    return {
      selectedMesage: ''
      } 
  },
  props: {
    id: { type: String, default: '' },
    text: { type: String, default: '' },
    name: { type: String, default: '' },
    photoUrl: { type: String, default: '' },
    sender: { type: Boolean, default: false },
    selectedMessage:  { type: Boolean, default: false }
  },

methods: {
      computedCSS: function(sender,selectedMessage) {
      if(sender){
        return 'textReceive bg-neutral-200 disabled'
      } else if(selectedMessage) {
       return 'textSend bg-blue-500'
      } else {
      return 'textSend bg-neutral-500'
      } 
    },
  greet: function(event){

    if (event) {
      if(!this.sender){
 this.$emit('clicked', {name : this.name, text: this.text})
      this.$store.commit('SET_SELECTED', this.id)
      }
       
    }
  }
}
}
</script>

