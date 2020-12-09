<template>
  <section class="main-top">
    <div class="main-top-logo">
      <router-link to="/main" exact>
        <img :src="logoImg" alt="logo" />
      </router-link>
    </div>
    <div class="main-top-user">
      <a-dropdown placement="bottomRight">
        <div>
          <span>{{ user_id }}</span>
          <a-icon type="down" />
        </div>
        <a-menu class="main-top-user-menu" slot="overlay">
          <a-menu-item v-if="user_token" @click="userAction" data-name="logout">
            <a-icon type="key" />
            <span>Log Out</span>
          </a-menu-item>
          <a-menu-item v-else @click="userAction" data-name="login">
            <a-icon type="key" />
            <span>Log In</span>
          </a-menu-item>
        </a-menu>
      </a-dropdown>
    </div>
  </section>
</template>

<script>
import { mapState, mapActions } from "vuex";

import logoImg from "../../../assets/nav_logo.png";

export default {
  name: "Main-top",
  data() {
    return {
      placements: ["bottomRight"],
      logoImg,
    };
  },

  methods: {
    userAction(e) {
      // console.log(e.target, "?????????");
      const { name } = e.domEvent.target.dataset;
      // console.log(name);
      name === "logout" || e.target === undefined
        ? this.$alert
            .fire({
              title: "로그아웃 성공!",
              timer: 2000,
              icon: "success",
              showConfirmButton: false,
            })
            .then(() => {
              // NOTE timing! it should be wait before get e.target
              this.removeTokenAction();
              this.$router.push(`/`);
            })
        : this.$router.push(`/`);
    },

    ...mapActions("users", ["removeTokenAction"]),
  },

  computed: {
    ...mapState({
      user_id: ({ users }) => users.user_id,
      user_token: ({ users }) => users.user_token,
    }),
  },
};
</script>

<style src="./Main-top.scss" lang="scss" scoped />
