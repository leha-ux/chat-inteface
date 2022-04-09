<template>
  <n-config-provider :theme-overrides="themeOverrides">
<div class="ml-28 mt-4 items-center">
    <n-space>
    Do you want to customize your avatar?
    <n-switch v-model:value="active" />
  </n-space>
</div>
  <n-grid v-if="active" :cols="6">
<n-gi :span="2">
<Avataaars
:topType="topValue"
:skinColor="skinColorValue"
:accessoriesType="accessoriesValue"
:hairColor="hairColorValue"
:facialHairType="facialhairTypeValue"
:eyeType="eyeTypeValue"
:eyebrowType="eyebrowValue" 
:mouthType="mouthValue"
:facialHairColor="facialHairColorValue"
:clotheType="clotheTypeValue"
:clotheColor="clotheColorValue"
:eyeColor="eyeColorValue"
>
</Avataaars>
</n-gi>

<n-gi
class="ml-8 mt-4"
:span="2">
<n-space vertical justify="space-around">
<div>Top
<n-select @update:value="onUpdate" placeholder="top" v-model:value="topValue" :options="topOptions" />  </div>
Hair Color
<n-select @update:value="onUpdate" placeholder="hair color" v-model:value="hairColorValue" :options="hairColorOptions" />
Eye color 
<n-select @update:value="onUpdate" placeholder="eye color" v-model:value="eyeColorValue" :options="eyeColorOptions" />
</n-space>
</n-gi>
<n-gi class="ml-8 mt-4" :span="2">
<n-space vertical justify="space-around">
<div>
Facial Hair
<n-select @update:value="onUpdate" placeholder="facial hair" v-model:value="facialhairTypeValue" :options="facialhairTypeOptions" /> </div>
Facial Hair Color
<n-select @update:value="onUpdate" placeholder="facial hair color" v-model:value="facialHairColorValue" :options="hairColorOptions" />
Eye
<n-select  @update:value="onUpdate" placeholder="eye" v-model:value="eyeTypeValue" :options="eyeTypeOptions" />
</n-space>
</n-gi>
<n-gi :span="2" class="ml-8 mt-2">
<n-space vertical justify="space-around">
Eyebrow
<n-select @update:value="onUpdate" placeholder="eyebrow" v-model:value="eyebrowValue" :options="eyebrowOptions" />
Mouth
<n-select @update:value="onUpdate" placeholder="mouth type" v-model:value="mouthValue" :options="mouthOptions" />
</n-space>
</n-gi>
<n-gi :span="2" class="ml-8 mt-2">
<n-space vertical justify="space-around">
Accessories
<n-select @update:value="onUpdate" placeholder="accessories" v-model:value="accessoriesValue" :options="accessoriesOptions" />
Skin 
<n-select @update:value="onUpdate" placeholder="skin color" v-model:value="skinColorValue" :options="skinColorOptions" />
</n-space>
</n-gi>
<n-gi :span="2" class="ml-8 mt-2">
<n-space vertical justify="space-around">
Clothe 
<n-select @update:value="onUpdate" placeholder="clothe type" v-model:value="clotheTypeValue" :options="clotheTypeOptions" />
Clothe color 
<n-select @update:value="onUpdate" placeholder="clothe color" v-model:value="clotheColorValue" :options="clotheColorOptions" />
</n-space>
</n-gi>
</n-grid>
  </n-config-provider>
</template>


<script>
/* eslint-disable */
import { watch, ref, computed, getCurrentInstance } from 'vue';
import { useStore } from 'vuex';
import Avataaars from './Avataaars.vue'

export default {
  components: {
    Avataaars
  },
  setup() {
const active = ref(false)
const store = useStore()

const themeOverrides = {
    common: {
      primaryColor: '#1a89fa',
      primaryColorHover: '#1a89fa',
    },
    Button: {
      textColor: '#1a89fa'
    },
    Select: {
      peers: {
        InternalSelection: {
          textColor: '#1a89fa'
        }
      }
    }
}

const topValue = ref(null)
const accessoriesValue = ref(null)
const facialhairTypeValue = ref(null)
const hairColorValue = ref(null)
const eyeTypeValue = ref(null)
const eyebrowValue = ref(null)
const mouthValue = ref(null)
const skinColorValue = ref(null)
const facialHairColorValue = ref(null)
const eyeColorValue = ref(null)
const clotheTypeValue = ref(null)
const clotheColorValue = ref(null)

const topOptions = [   
{
label: "NoHair",
value : "NoHair"
},
{
label: "Hat",
value : "Hat",
},
{
label: "Hijab",
value : "Hijab",
},
{
label: "Turban",
value : "Turban",
},
{
label: "WinterHat1",
value : "WinterHat1",
},
{
label: "LongHairBigHair",
value : "LongHairBigHair",
},

{
label: "LongHairBob",
value : "LongHairBob",
},
{
label: "LongHairBun",
value : "LongHairBun",
},
{
label: "LongHairCurly",
value : "LongHairCurly",
},
{
label: "LongHairDreads",
value : "LongHairDreads",
},
{
label: "LongHairFrida",
value : "LongHairFrida",
},
{
label: "LongHairFro",
value : "LongHairFro",
},
{
label: "LongHairFroBand",
value : "LongHairFroBand",
},
{
label: "LongHairNotTooLong",
value : "LongHairNotTooLong",
},
{
label: "LongHairShavedSides",
value : "LongHairShavedSides",
},
{
label: "LongHairMiaWallace",
value : "LongHairMiaWallace",
},
{
label: "LongHairStraight",
value : "LongHairStraight",
},
{
label: "LongHairStraight2",
value : "LongHairStraight2",
},
{
label: "LongHairStraightStrand",
value : "LongHairStraightStrand",
},
{
label: "ShortHairDreads01",
value : "ShortHairDreads01",
},
{
label: "ShortHairDreads02",
value : "ShortHairDreads02",
},
{
label: "ShortHairFrizzle",
value : "ShortHairFrizzle",
},
{
label: "ShortHairShaggy",
value : "ShortHairShaggy",
},
{
label: "ShortHairShaggyMullet",
value : "ShortHairShaggyMullet",
},
{
label: "ShortHairShortCurly", 
value : "ShortHairShortCurly", 
},
{
label: "ShortHairShortFlat", 
value : "ShortHairShortFlat", 
},
{
label: "ShortHairShortRound",
value : "ShortHairShortRound",
},
{
label: "ShortHairShortWaved",
value : "ShortHairShortWaved",
},
{
label: "ShortHairSides",
value : "ShortHairSides",
},
{
label: "ShortHairTheCaesar",
value : "ShortHairTheCaesar",
},
{
label: "ShortHairTheCaesarSidePart",
value : "ShortHairTheCaesarSidePart",
},
];
const accessoriesOptions = [
{
label: "Blank",
value : "Blank",
},
{
label: "Kurt",
value : "Kurt",
},
{
label: "Prescription01",
value : "Prescription01",
},
{
label: "Prescription02",
value : "Prescription02",
},
{
label: "Round",
value : "Round",
},
{
label: "Sunglasses",
value : "Sunglasses",
},
{
label: "Wayfarers",
value : "Wayfarers",
},
]
const facialhairTypeOptions = [
    {
        label: "Blank",
        value: "Blank"
    },
    {
        label: "BeardMedium",
        value: "BeardMedium"
    },
    {
        label: "BeardLight",
        value: "BeardLight"
    },
    {
        label: "BeardMajestic",
        value: "BeardMajestic"
    },
    {
        label: "MoustacheFancy",
        value: "MoustacheFancy"
    },
    {
        label: "MoustacheMagnum",
        value: "MoustacheMagnum"
    },
   
]
const hairColorOptions = [
    {
        label: "Auburn",
        value: "Auburn", 
    },
    {
        label: "Black",
        value: "Black", 
    },
    {
        label: "Blonde",
        value: "Blonde", 
    },
    {
        label: "BlondeGolden",
        value: "BlondeGolden", 
    },
    {
        label: "Brown",
        value: "Brown", 
    },
    {
        label: "BrownDark",
        value: "BrownDark", 
    },
    {
        label: "PastelPink",
        value: "PastelPink", 
    },
    {
        label: "Platinum",
        value: "Platinum", 
    },
    {
        label: "Red",
        value: "Red", 
    },
    {
        label: "SilverGray",
        value: "SilverGray", 
    },
]
const eyeTypeOptions = [
    {
        label: "Close",
        value: "Close"
    },
    {
        label: "Cry",
        value: "Cry"
    },
    {
        label: "Default",
        value: "Default"
    },
    {
        label: "Dizzy",
        value: "Dizzy"
    },
    {
        label: "EyeRoll",
        value: "EyeRoll"
    },
    {
        label: "Happy",
        value: "Happy"
    },
    {
        label: "Hearts",
        value: "Hearts"
    },
    {
        label: "Side",
        value: "Side"
    },
    {
        label: "Squint",
        value: "Squint"
    },
    {
        label: "Wink",
        value: "Wink"
    },
    {
        label: "WinkWacky",
        value: "WinkWacky"
    },
]
const eyebrowOptions = [
    {
        label: "Angry",
        value: "Angry"
    },
    {
        label: "AngryNatural",
        value: "AngryNatural"
    },
    {
        label: "Default",
        value: "Default"
    },
    {
        label: "DefaultNatural",
        value: "DefaultNatural"
    },
    {
        label: "FlatNatural",
        value: "FlatNatural",
    },
    {
        label: "FrownNatural",
        value: "FrownNatural",
    },
    {
        label: "RaisedExcited",
        value: "RaisedExcited"
    },
    {
        label: "RaisedExcitedNatural",
        value: "RaisedExcitedNatural"
    },
    {
        label: "SadConcerned",
        value: "SadConcerned"
    },
    {
        label: "SadConcernedNatural",
        value: "SadConcernedNatural"
    },
    {
        label: "UnibrowNatural",
        value: "UnibrowNatural"
    },
    {
        label: "UpDown",
        value: "UpDown"
    },
    {
        label: "UpDownNatural",
        value: "UpDownNatural"
    },
]
const mouthOptions = [{
label: "Concerned",
value : "Concerned",
},
{
label: "Default",
value : "Default",
},
{
label: "Disbelief",
value : "Disbelief",
},
{
label: "Eating",
value : "Eating",
},
{
label: "Grimace",
value : "Grimace",
},
{
label: "Sad",
value : "Sad",
},
{
label: "ScreamOpen",
value : "ScreamOpen",
},
{
label: "Serious",
value : "Serious",
},
{
label: "Smile",
value : "Smile",
},
{
label: "Tongue",
value : "Tongue",
},
{
label: "Twinkle",
value : "Twinkle",
},
{
label: "Vomit",
value : "Vomit",
},
]
const skinColorOptions = [
    {
        label: "Tanned",
        value: "Tanned",
    },
    {
        label: "Yellow",
        value: "Yellow",
    },
    {
        label: "Pale",
        value: "Pale",
    },
    {
        label: "Light",
        value: "Light",
    },
    {
        label: "Brown",
        value: "Brown",
    },
    {
        label: "DarkBrown",
        value: "DarkBrown",
    },
    {
        label: "Black",
        value: "Black",
    },
]
const eyeColorOptions = [
    {
        label: "Black",
        value: "Black"
    },
    {
        label: "Blue01",
        value: "Blue01"
    },
    {
        label: "Blue02",
        value: "Blue02"
    },
    {
        label: "Gray",
        value: "Gray"
    },
    {
        label: "Green",
        value: "Green"
    },
    {
        label: "Brown",
        value: "Brown"
    },
]
const clotheTypeOptions = [
{
    label: "BlazerShirt",
    value: "BlazerShirt",
},
{
    label: "BlazerSweater",
    value: "BlazerSweater",
},
{
    label: "CollarSweater",
    value: "CollarSweater",
},
{
    label: "GraphicShirt",
    value: "GraphicShirt",
},
{
    label: "Hoodie",
    value: "Hoodie",
},
{
    label: "Overall",
    value: "Overall",
},
{
    label: "ShirtCrewNeck",
    value: "ShirtCrewNeck",
},
{
    label: "ShirtScoopNeck",
    value: "ShirtScoopNeck",
},
{
    label: "ShirtVNeck",
    value: "ShirtVNeck",
},
]

const clotheColorOptions = [
    {
        label: "Black",
        value: "Black",
    },
    {
        label: "Blue01",
        value: "Blue01",
    },
    {
        label: "Blue02",
        value: "Blue02",
    },
    {
        label: "Blue03",
        value: "Blue03",
    },
    {
        label: "Gray01",
        value: "Gray01",
    },
    {
        label: "Gray02",
        value: "Gray02",
    },
    {
        label: "Heather",
        value: "Heather",
    },
    {
        label: "PastelBlue",
        value: "PastelBlue",
    },
    {
        label: "PastelGreen",
        value: "PastelGreen",
    },
    {
        label: "PastelOrange",
        value: "PastelOrange",
    },
    {
        label: "PastelRed",
        value: "PastelRed",
    },
    {
        label: "PastelYellow",
        value: "PastelYellow",
    },
    {
        label: "Pink",
        value: "Pink",
    },
    {
        label: "Red",
        value: "Red",
    },
    {
        label: "White",
        value: "White",
    },
]

const onUpdate = (values) => {
store.commit('SET_AVATAR', 
{'topValue' : topValue.value,
'skinColorValue' : skinColorValue.value, 
'accessoriesValue' : accessoriesValue.value,
'hairColorValue' : hairColorValue.value,
'facialhairTypeValue' : facialhairTypeValue.value,
'eyeTypeValue' : eyeTypeValue.value,
'eyebrowValue' : eyebrowValue.value,
'mouthValue' : mouthValue.value, 
'facialHairColorValue' : facialHairColorValue.value, 
'clotheTypeValue' : clotheTypeValue.value,
'clotheColorValue' : clotheColorValue.value,
'eyeColorValue' : eyeColorValue.value,
})};


return {
    topValue,
    accessoriesValue,
    facialhairTypeValue,
    hairColorValue,
    eyeTypeValue,
    eyebrowValue,
    mouthValue,
    skinColorValue,
    facialHairColorValue,
    eyeColorValue,
    clotheTypeValue,
    clotheColorValue,
    topOptions,
    accessoriesOptions,
    facialhairTypeOptions,
    hairColorOptions,
    eyeTypeOptions,
    eyebrowOptions,
    mouthOptions,
    skinColorOptions,
    eyeColorOptions,
    clotheTypeOptions,
    clotheColorOptions,
    themeOverrides,
    onUpdate,
    active,
};

},
};
</script>

<style>

</style>




