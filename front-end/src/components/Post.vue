<template>
  <div>
    <h1 v-if="msg">
      {{ msg }}
      <h3 v-if="user">name: {{ user.name }} id: {{ user.id }}</h3>
    </h1>
  </div>
</template>

<script>
export default {
  name: "Post",
  props: ["user"],
  data() {
    return {
      msg: "bananas",
      err: null,
    };
  },
};
</script>

