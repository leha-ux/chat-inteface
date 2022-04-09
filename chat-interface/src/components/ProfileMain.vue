<template>
<Avataaars
:class="size"
:topType="attributes.topValue"
:skinColor="attributes.skinColorValue"
:accessoriesType="attributes.accessoriesValue"
:hairColor="attributes.hairColorValue"
:facialHairType="attributes.facialhairTypeValue"
:eyeType="attributes.eyeTypeValue"
:eyebrowType="attributes.eyebrowValue" 
:mouthType="attributes.mouthValue"
:facialHairColor="attributes.facialHairColorValue"
:clotheType="attributes.clotheTypeValue"
:clotheColor="attributes.clotheColorValue"
:eyeColor="attributes.eyeColorValue"
>
</Avataaars>

</template>
<script>
/* eslint-disable */
import { computed } from 'vue'
import Avataaars from './Avataaars.vue'

export default {
    components: {
    Avataaars
  },
  props: { size: { type: String, default: 'w-14' },
  attributes: {type: Object} },

computed: {
}
}


</script>
