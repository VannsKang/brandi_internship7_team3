<template>
  <a-layout class="sellerInfo">
    <div>
      <sellers-header :header="sellerInfo_header" />

      <a-layout-content class="sellerInfo-content">
        <div class="sellerInfo-content-header">
          <div>
            <a-icon type="user" />
            <span>기본 정보</span>
          </div>
        </div>
        <div class="sellerInfo-content-table">
          <table>
            <tbody>
              <tr>
                <td>셀러 프로필 <label class="font-color-red">*</label></td> 
                <td>
                  <div class="seller-profile-thumbnail">
                    <img :src="noImg" alt="noimage">
                  </div>
                  <div>
                    <a-button>이미지 선택</a-button>
                  </div>
                  <div class="padding-top-10">
                    <div class="sellerInfo-content-table-font-blue">
                      <a-icon type="info-circle" />
                      셀러 프로필 확장자는
                      <span class="font-bold">jpg, jpeg, png</span>
                        만 가능하며, 허용 가능한 최대 파일사이즈 크기는
                      <span class="font-bold">5MB</span> 
                      입니다.</div>
                  </div>
                </td>
              </tr>
              <tr>
                <td>셀러 상태</td>
                <td>퇴점대기</td>
              </tr>
              <tr>
                <td>
                  셀러 속성  <label class="font-color-red">*</label>
                </td>
                <td>
                  <a-radio-group name="radioGroup" :default-value="1">
                    <a-radio :value="1">
                      쇼핑몰
                    </a-radio>
                    <a-radio :value="2">
                      마켓
                    </a-radio>
                    <a-radio :value="3">
                      로드샵
                    </a-radio>
                  </a-radio-group>
                </td>
              </tr>
              <tr>
                <td>
                  셀러 한글명
                </td>
                <td>
                  <div class="input-size">
                    <a-input ref="userNameInput" v-model="userName" placeholder="셀러 한글명">
                      <a-icon slot="prefix" type="user" />
                    </a-input>
                  </div>
                </td>
              </tr>
              <tr>
                <td>셀러 영문명</td>
                <td>
                  <div class="input-size">
                    <a-input ref="userNameInput" v-model="userName" placeholder="셀러 영문명">
                      <a-icon slot="prefix" type="user" />
                    </a-input>
                  </div>
                </td>
              </tr>
              <tr>
                <td>셀러 계정</td>
                <td>
                  <span>셀러 아이디</span>
                    <a-button type="danger" class="btn-size" @click="passwordChangeShowModal">
                      비밀번호 변경하기
                    </a-button>
                    <a-modal v-model="visible" title="비밀번호 변경하기" on-ok="passwordChangeShowModalHandleOk">
                      <template slot="footer">
                        <a-button key="back" @click="passwordChangeShowModalHandleCancel">
                          취소
                        </a-button>
                        <a-button key="submit" type="success" :loading="loading" @click="passwordChangeShowModalHandleOk">
                          변경
                        </a-button>
                      </template>
                      <p>변경할 비밀번호</p>
                      <a-input class="margin-bottom-10" ref="userNameInput" v-model="userName" placeholder="변경할 비밀번호">
                      </a-input>
                      <br>
                      <p>비밀번호 재입력</p>
                      <a-input ref="userNameInput" v-model="userName" placeholder="한번 더 입력해주세요.">
                      </a-input>
                   </a-modal>
                </td>
              </tr>
            </tbody>
          </table>
        </div>
      </a-layout-content>
      <a-layout-content class="sellerInfo-content">
        <div class="sellerInfo-content-header">
          <div>
            <a-icon type="user" />
            <span>상세 정보</span>
          </div>
        </div>
        <div class="sellerInfo-content-table">
          <table>
            <tbody>
              <tr>
                <td>셀러페이지 배경이미지 <label class="font-color-red">*</label></td> 
                <td>
                  <div class="seller-profile-thumbnail">
                    <img :src="noImg" alt="noimage">
                  </div>
                  <div>
                    <a-button>이미지 선택</a-button>
                  </div>
                  <div class="padding-top-10">
                    <div class="sellerInfo-content-table-font-blue">
                      <a-icon type="info-circle" />
                      브랜디 앱과 웹 사이트의 셀러 페이지에 보여질 배경이미지 입니다.
                      <br>
                      <a-icon type="info-circle" />
                      배경이미지는 
                      <span class="font-bold">1200 * 850</span>
                        사이즈 이상으로 등록해주세요.
                      <br>
                      <a-icon type="info-circle" />
                      확장자는
                      <span class="font-bold">jpg, jpeg, png</span>
                        만 가능하며, 허용 가능한 최대 파일사이즈 크기는
                      <span class="font-bold">5MB</span> 
                      입니다.
                      </div>
                  </div>
                </td>
              </tr>
              <tr>
                <td>
                  셀러 한줄 소개 <label class="font-color-red">*</label></td>
                <td>
                  <div class="input-size">
                    <a-input ref="userNameInput" v-model="userName" placeholder="셀러 한줄 소개">
                    <a-icon slot="prefix" type="user" />
                  </a-input>
                  </div>
                </td>
              </tr>
              <tr>
                <td>
                  셀러 상세 소개
                </td>
                <td>
                  <div>
                    <div class="input-size">
                      <a-textarea placeholder="셀러 상세 소개" :rows="4" allow-clear @change="onChange"/>
                    </div>
                  </div>
                  <div class="sellerInfo-content-table-font-blue">
                    <a-icon type="info-circle" />
                    셀러 상세 소개 글은 최소 10자 이상입니다.
                  </div>
                </td>
              </tr>
              <tr>
                <td>담당자 정보 <label class="font-color-red">*</label></td>
                <td>
                  <div>
                    <div class="margin-bottom-5 input-size">
                      <a-input ref="userNameInput" v-model="userName" placeholder="담당자명">
                        <a-icon slot="prefix" type="user" />
                      </a-input>
                    </div>
                    <div class="margin-bottom-5 input-size">
                      <a-input ref="userNameInput" v-model="userName" placeholder="담당자 핸드폰번호">
                      <a-icon slot="prefix" type="phone" />
                      </a-input>
                    </div>
                    <div class="margin-float input-size"> 
                      <a-input ref="userNameInput" v-model="userName" placeholder="담당자 이메일">
                      <a-icon slot="prefix" type="mail" />
                      </a-input>
                    </div>
                  </div>
                  <div class="font-bold">
                    <a-button type="success">
                      <a-icon type="plus" />
                      </a-button>
                    </div>
                </td>
              </tr>
              <tr>
                <td>고객 센터 <label class="font-color-red">*</label></td>
                <td>
                  <div class="input-size">
                    <a-input ref="userNameInput" v-model="userName" placeholder="고객센터 전화번호">
                    <a-icon slot="prefix" type="phone" />
                  </a-input>
                  </div>
                </td>
              </tr>
              <tr>
                <td>택배 주소 <label class="font-color-red">*</label></td>
                <td>

                </td>
              </tr>
              <tr>
                <td>고객센터 운영시간 (주중) <label class="font-color-red">*</label></td>
                <td>
                  
                   <div class="sellerInfo-content-table-font-blue">
                    <a-icon type="info-circle" />
                    주말 및 공휴일에도 운영하시는 경우 체크박스를 누르시고 입력해주세요. 
                  </div>
                    <a-checkbox @change="onChange"></a-checkbox>

                </td>
              </tr>
            </tbody>
          </table>
        </div>
      </a-layout-content>
    </div>
  </a-layout>
</template>

<script>
import { mapState } from "vuex";

// LINK component
import SellersHeader from "../components/Sellers-header/Sellers-header";
import noImg from "../../assets/no_image.png";

export default {
  name: "SellerInfo",

  components: {
    "sellers-header": SellersHeader,
  },

  data() {
    return {
      noImg,
      userName: '',
      visible: false,
      confirmLoading: false,
      loading: false,
    };
  },

  computed: {
    ...mapState({
      sellerInfo_header: ({ sellerInfo }) => sellerInfo.sellerInfo_header,
    }),
  },

  methods: {
    emitEmpty() {
      this.$refs.userNameInput.focus();
      this.userName = '';
    },
    onChange(e) {
      console.log(e);
    },
    onChange(e) {
      console.log(`checked = ${e.target.checked}`);
    },
     passwordChangeShowModal() {
      this.visible = true;
    },
    passwordChangeShowModalHandleOk(e) {
      this.loading = true;
      setTimeout(() => {
        this.visible = false;
        this.loading = false;
      }, 3000);
    },
    passwordChangeShowModalHandleCancel(e) {
      this.visible = false;
    },
  },
};

</script>

<style lang="scss" scoped>
@import "../../styles/mixin.scss";

.sellerInfo {
  overflow: auto;
  &-content {
    margin: 10px 20px 25px;
    background: #fff;
    border: 1px solid #ddd;
    border-radius: 4px;

    &-header {
      width: 100%;
      height: 38px;
      padding: 0 10px;
      border-radius: 4px 4px 0 0;
      background: #eee;

      @include flexSet("space-between", "center");

      > div {
        @include flexSet("flex-start", "center");

        &:first-child {
          color: #111;

          span {
            margin-left: 5px;
            font-size: 16px;
          }
        }
      }
    }

    &-table {
      padding: 10px;
      > table {
        border-collapse: collapse;
        margin-bottom: 20px;
        max-width: 100%;
        width: 100%;

        > tbody > tr {
          &:nth-child(odd) > td {
            background-color: #f9f9f9;
          } 

          > td {
            padding: 8px;
            border: 1px solid #ddd;
            vertical-align: middle;
            margin-right: 5px;
            
            &:nth-child(odd) {
              width: 15%;
            } 
          }
        }
        
      }
      img {
        width: 90px;
        height: 90px;
      }

      &-font-blue {
        color: #1e90ff;
      }
      
    }
  }
}

.font-bold {
  font-weight: bold;
}

.font-color-red {
  color: #ff0000;
}

.padding-top-10 {
  padding-top: 10px;
}

.seller-profile-thumbnail {
  border: 1px solid #ddd;
  padding: 4px;
  margin-bottom: 5px;
  width: 100px;
  height: 100px;
}

.ant-btn-danger {
  background-color: #ff4d4f;
  border-color: #ff4d4f;
}

.ant-btn-danger:focus, .ant-btn-danger:hover {
  background-color: #ff7875;
  border-color: #ff7875;
  color: #fff;
}

.ant-btn-success {
  background-color: #5cb85c;
  border-color: #5cb85c;
  color: #fff;
}

.btn-size {
  font-size: 12px;
  padding: 1px 5px;
  line-height: 1.5;
  height: 25px;
}

.input-size {
  width: 41.666667%;
  padding-right: 15px;
}

.textarea-input-size {
  min-height: 100px;
}

.margin-bottom-5 {
  margin-bottom: 5px;
}

.margin-bottom-10 {
  margin-bottom: 10px;
}

.margin-float {
  float: left;
  max-width: 100%;
}
/* 여기다 css */
</style>

