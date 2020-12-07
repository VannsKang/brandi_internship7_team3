<template>
  <section class="main-footer">
    <div>
      <span> {{ footer_text }}{{ email }} </span>
      <span>{{ copyright }}</span>
    </div>
  </section>
</template>

<script>
import { mapState, mapActions } from "vuex";

export default {
  name: "Main-footer",

  mounted() {
    this.updateFooterAction();
  },

  computed: {
    ...mapState({
      footer_text: ({ navmenus }) => navmenus.footer_text,
      copyright: ({ navmenus }) => navmenus.copyright,
      email: ({ navmenus }) => navmenus.email,
    }),
  },

  methods: {
    ...mapActions("navmenus", ["updateFooterAction"]),
  },
};
</script>

<style src="./Main-footer.scss" lang="scss" scoped />
