<template>
  <img :src="require(`~/assets/img/${imageName}.svg`)" />
</template>

<script>
export default {
  name: "IconBase",
  props: {
    imageName: {
      type: String,
      require: false,
    },
  },
};
</script>

<style scoped></style>
