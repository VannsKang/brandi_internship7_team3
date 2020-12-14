<template>
  <div class="sellers-content-main-pagination">
    <span>Page</span>
    <div class="sellers-content-main-pagination-button">
      <a-button
        data-id="minus"
        @click="controlPagesAction"
        :disabled="page_number <= 1 || max_page <= 1"
      >
        <a-icon type="left" />
      </a-button>
      <!-- SECTION pagenation number -->
      <a-input-number :value="page_number" />

      <a-button
        data-id="plus"
        @click="controlPagesAction"
        :disabled="page_number >= max_page"
      >
        <a-icon type="right" />
      </a-button>
    </div>
    <span>of {{ max_page }} | View</span>
    <a-select
      class="sellers-content-main-pagination-group"
      :value="currentPagination"
      @change="controlPagesDrop"
    >
      <a-select-option
        v-for="(page, idx) in pageControl"
        :value="page"
        :key="idx"
      >
        {{ page }}
      </a-select-option>
    </a-select>
    <span>records | Found total {{ seller_count }} records</span>
  </div>
</template>

<script>
import { mapState, mapActions, mapGetters } from "vuex";

export default {
  name: "Sellers-pagination",

  props: {},

  data() {
    return {};
  },

  methods: {
    // SECTION vuex
    ...mapActions("sellers", ["controlPagesAction", "controlPagesDrop"]),
  },

  computed: {
    ...mapState({
      pageControl: ({ sellers }) => sellers.pageControl,
      page_number: ({ sellers }) => sellers.page.page_number,
      currentPagination: ({ sellers }) => sellers.page.currentPagination,
      seller_count: ({ sellers }) => sellers.seller_count,
    }),
    ...mapGetters("sellers", ["max_page", "update_page"]),
  },
};
</script>

<style src="./Sellers-pagination.scss" lang="scss" scoped />
