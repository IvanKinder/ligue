<template>
  <div>
    {{ playbooks }}
  </div>
</template>

<script>
import axios from 'axios';

export default {
  name: 'Playbooks',
  data() {
    return {
      playbooks: [],
    };
  },
  methods: {
    getMessage() {
      const path = 'http://localhost:5000/playbooks';
      axios.get(path)
        .then((res) => {
          this.playbooks = res.data;
        })
        .catch((error) => {
          this.playbooks = error;
        });
    },
  },
  created() {
    this.getMessage();
  },
};
</script>

<style scoped>

</style>
