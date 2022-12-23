<template>
  <div>
    <MyButton btnName="Get playbooks" url="/playbooks/"/>
  </div>
</template>

<script>
import MyButton from './MyButton';

export default {
  name: 'Client',
  components: { MyButton },
  data() {
    return {
      msg: '',
    };
  },
};
</script>
