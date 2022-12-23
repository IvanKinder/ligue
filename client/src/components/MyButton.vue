<template>
  <div>
    <router-link :to="{ path: url}"> {{ btnName }} </router-link>
  </div>
</template>

<script>

export default {
  name: 'MyButton',
  props: {
    btnName: String,
    url: String,
  },
};
</script>

<style scoped>

</style>
