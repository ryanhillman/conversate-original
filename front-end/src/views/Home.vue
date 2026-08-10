<template>
  <div>
    <hero />
  </div>
</template>

<script>
import Hero from "../components/Hero.vue";
export default {
  name: "home",
  components: {
    Hero,
  },
  data() {
    return {

    };
  },
  mounted() {

  },
  methods: {

  },
};
</script>

<style lang="scss" scoped>
.next-steps {
  .fa-link {
    margin-right: 5px;
  }
}
.btn-new {
    background-color: #2A3F54;
}
</style>
