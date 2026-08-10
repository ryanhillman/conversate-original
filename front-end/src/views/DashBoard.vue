<template>
  <div class="container">
    <div>
      <Mastery /> 
    </div>
    <br />
    <br />
  </div>
</template>


<script>
import Mastery from "../components/Dashboard/Mastery.vue";
import SetUserName from "../components/General/SetUserName.vue"
export default {
  name: "dashboard",
  components: {
    Mastery,
    SetUserName
  },
  data() {
    return {

    };
  },
  mounted() {},
  methods: {},
};
</script>