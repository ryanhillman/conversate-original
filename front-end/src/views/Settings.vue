<template>
  <div class="container">
    <div class="row align-items-center profile-header">
      <div class="col-md-2 mb-3">
        <img
          :src="$auth.user.picture"
          alt="User's profile picture"
          class="rounded-circle img-fluid profile-picture"
        />
      </div>
      <div class="col-md text-center text-md-left">
        <h2>{{ $auth.user.name }}</h2>
        <p class="lead text-muted">{{ $auth.user.email }}</p>
      </div>
      <div class="col-md text-center text-md-left">
          <EditUserName />
      </div>
    </div>
  </div>
</template>

<script>
import EditUserName from '../components/General/EditUserName.vue';
export default {
  name: "settings",
  components: {
    EditUserName
    
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
