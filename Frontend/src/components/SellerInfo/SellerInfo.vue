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
                    <img v-if="profileImageUrl" :src="profileImageUrl" alt="업로드할 이미지"/>
                    <img v-else-if="sellerInfo.seller_profile" :src="sellerInfo.seller_profile" alt="profile_img" />
                    <img v-else :src="noImg" alt="noimage">
                  </div>
                  <div v-if="profileImageUrl">
                    <a-upload
                    name="file"
                    class="avatar-uploader"
                    :show-upload-list="false"
                    action="https://www.mocky.io/v2/5cc8019d300000980a055e76"
                    :headers="headers"
                    :before-upload="beforeUpload"
                    @change="onClickImageUpload"
                    >
                    <a-button>변경</a-button>
                    </a-upload>
                     <a-button type="danger" @click="onClickImageDelete">삭제</a-button>
                  </div>
                  <div v-else>
                    <a-upload
                    name="file"
                    class="avatar-uploader"
                    :show-upload-list="false"
                    action="https://www.mocky.io/v2/5cc8019d300000980a055e76"
                    :headers="headers"
                    :before-upload="beforeUpload"
                    @change="onClickImageUpload"
                    >
                    <a-button>이미지 선택</a-button>
                    </a-upload>
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
                <td>{{ sellerInfo.seller_status }}</td>
              </tr>
              <tr>
                <td>
                  셀러 속성  <label class="font-color-red">*</label>
                </td>
                <td>
                  <a-radio-group name="radioGroup" v-model="sellerInfo.seller_attribute_id">
                    <a-radio v-for="attribute in attributeInfo" 
                    :value="attribute.seller_attribute_id"
                    :key="attribute.seller_attribute_id">
                      {{ attribute.name }}
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
                    <a-input ref="userNameInput" v-model="sellerInfo.kor_name" placeholder="셀러 한글명">
                      <a-icon slot="prefix" type="user" />
                    </a-input>
                  </div>
                </td>
              </tr>
              <tr>
                <td>셀러 영문명</td>
                <td>
                  <div class="input-size">
                    <a-input ref="userNameInput" v-model="sellerInfo.eng_name" placeholder="셀러 영문명">
                      <a-icon slot="prefix" type="user" />
                    </a-input>
                  </div>
                </td>
              </tr>
              <tr>
                <td>셀러 계정</td>
                <td>
                  <span>{{ sellerInfo.seller_id }}</span>
                    <a-button type="danger" class="btn-size" @click="passwordChangeShowModal">
                      비밀번호 변경하기
                    </a-button>
                    <a-modal v-model="passwordModalVisible" title="비밀번호 변경하기" on-ok="passwordChangeShowModalHandleOk">
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
                    <img v-if="backgroundImageUrl" :src="backgroundImageUrl" alt="업로드할 이미지"/>
                    <img v-else-if="sellerInfo.seller_background" :src="sellerInfo.seller_background" alt="backgroun_img" />
                    <img v-else :src="noImg" alt="noimage">
                  </div>
                  <div v-if="backgroundImageUrl">
                    <a-upload
                    name="file"
                    class="avatar-uploader"
                    :show-upload-list="false"
                    action="https://www.mocky.io/v2/5cc8019d300000980a055e76"
                    :headers="headers"
                    :before-upload="beforeUpload"
                    @change="onClickBackgroundImageUpload"
                    >
                    <a-button>변경</a-button>
                    </a-upload>
                     <a-button type="danger" @click="onClickBackgroundImageDelete">삭제</a-button>
                  </div>
                  <div v-else>
                    <a-upload
                    name="file"
                    class="avatar-uploader"
                    :show-upload-list="false"
                    action="https://www.mocky.io/v2/5cc8019d300000980a055e76"
                    :headers="headers"
                    :before-upload="beforeUpload"
                    @change="onClickBackgroundImageUpload"
                    >
                    <a-button>이미지 선택</a-button>
                    </a-upload>
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
                    <a-input ref="userNameInput" v-model="sellerInfo.seller_intro" placeholder="셀러 한줄 소개">
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
                      <a-textarea placeholder="셀러 상세 소개" v-model="sellerInfo.seller_detail" :rows="4" allow-clear @change="onChange"/>
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
                      <a-input ref="userNameInput" v-model="sellerInfo.owner_name" placeholder="담당자명">
                        <a-icon slot="prefix" type="user" />
                      </a-input>
                    </div>
                    <div class="margin-bottom-5 input-size">
                      <a-input ref="userNameInput" v-model="sellerInfo.owner_number" placeholder="담당자 핸드폰번호">
                      <a-icon slot="prefix" type="phone" />
                      </a-input>
                    </div>
                    <div class="margin-float input-size"> 
                      <a-input ref="userNameInput" v-model="sellerInfo.owner_email" placeholder="담당자 이메일">
                      <a-icon slot="prefix" type="mail" />
                      </a-input>
                    </div>
                  </div>
                </td>
              </tr>
              <tr>
                <td>고객 센터 <label class="font-color-red">*</label></td>
                <td>
                  <div class="input-size">
                    <a-input ref="userNameInput" v-model="sellerInfo.cs_number" placeholder="고객센터 전화번호">
                    <a-icon slot="prefix" type="phone" />
                  </a-input>
                  </div>
                </td>
              </tr>
              <tr>
                <td>택배 주소 <label class="font-color-red">*</label></td>
                <td>
                  <div>
                    <div class="margin-bottom-5 margin-float input-size"> 
                        <a-input ref="userNameInput" v-model="sellerInfo.zipcode" placeholder="우편번호">
                        <a-icon slot="prefix" type="inbox" />
                        </a-input>
                    </div>
                    <div class="font-bold">
                      <a-button type="success" @click="zipCodeShowModal">
                      우편번호 찾기
                      </a-button>


                    </div>           
                    <div class="margin-bottom-5 input-size"> 
                      <a-input ref="userNameInput" v-model="sellerInfo.first_address" placeholder="주소 (택배 수령지)">
                      <a-icon slot="prefix" type="environment" />
                      
                      </a-input>
                    </div>
                    <div class="margin-bottom-5 input-size"> 
                      <a-input ref="userNameInput" v-model="sellerInfo.last_address" placeholder="상세주소 (택배 수령지)">
                      <a-icon slot="prefix" type="environment" />
                      </a-input>
                    </div>
                  </div>
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
      <a-layout-content class="sellerInfo-content">
        <div class="sellerInfo-content-header">
          <div>
            <a-icon type="user" />
            <span>배송정보 및 교환/환불 정보</span>
          </div>
        </div>
        <div class="sellerInfo-content-table">
          <table>
            <tbody>
              <tr>
                <td>배송정보 <label class="font-color-red">*</label></td> 
                <td>
                  <div class="textarea-input-size">
                      <a-textarea 
                      placeholder=
                      "ex) 
도서 산간 지역은 배송비가 추가비용이 발생할 수 있습니다.
결제 완료 후 1~3일 후 출고됩니다. 
                      " v-model="sellerInfo.delivery"
                       :rows="4" allow-clear @change="onChange"/>
                    </div>
                  <div class="sellerInfo-content-table-font-blue">
                    <a-icon type="info-circle" />
                    문장이 끝나면 엔터로 줄바꿈을 해주세요.
                  </div>
                </td>
              </tr>
              <tr>
                <td>교환/환불 정보 <label class="font-color-red">*</label></td>
                <td>
                  <div class="textarea-input-size">
                      <a-textarea placeholder="ex) 
브랜디는 소비자보호법 및 전자상거래법을 기반한 환불보장제를 운영 중에 있습니다.
정당하지 않은 사유로 인한 환불 거부 등은 제재 사유가 될수 있는 점 참고 부탁드립니다.
                      " v-model="sellerInfo.refund" :rows="4" allow-clear @change="onChange"/>
                    </div>
                    <div class="sellerInfo-content-table-font-blue">
                    <a-icon type="info-circle" />
                    문장이 끝나면 엔터로 줄바꿈을 해주세요.
                  </div>
                </td>
              </tr>
              
            </tbody>
          </table>
        </div>
      </a-layout-content>  
      <div class="font-bold align">
          <a-button type="success" @click="">
          수정
          </a-button>
          <a-button @click="">취소</a-button>
      </div>
    </div>
    
  </a-layout>
  
</template>

<script>
import { mapState } from "vuex";

// LINK component
import SellersHeader from "../components/Sellers-header/Sellers-header";
import noImg from "../../assets/no_image.png";
import DaumPostcode from 'vuejs-daum-postcode'
import { Modal } from 'ant-design-vue';
import {
  SELLER_DETAIL,
  SELLER_ATTRIBUTE_ID,
  SELLER_STATUS
} from "../../config";


function getBase64(img, callback) {
  const reader = new FileReader();
  reader.addEventListener('load', () => callback(reader.result));
  reader.readAsDataURL(img);
}

export default {
  name: "SellerInfo",

  components: {
    "sellers-header": SellersHeader,
    DaumPostcode,
  },

  data() {
    return {
      noImg,
      sellerInfo: {},
      attributeInfo: {},
      attribute: {},
      userName: '',
      zipcode: '',
      passwordModalVisible: false,
      confirmLoading: false,
      loading: false,
      zipcodeVisible: false,
      profileImageUrl: '',
      backgroundImageUrl: '',
    };
  },

  computed: {
    ...mapState({
      sellerInfo_header: ({ sellerInfo }) => sellerInfo.sellerInfo_header,
    }),
  },

  mounted() {
    this.getInfo();
  },

  methods: {
    async getInfo() {
      await this.getSellerInfo()
      await this.getAttributeInfo()
      this.getStatusInfo()
    },

    async getSellerInfo() {
      try {
        const response = await this.$http.get(SELLER_DETAIL);
        const validation = response && response.status === 200;
        !validation && new Error("cannot fetch the data");
        const result = response.data;
        this.sellerInfo = result

      } catch (error) {
        console.log("!!error fetch data!!")
      }
    },

    async getAttributeInfo() {
      try {
        const response = await this.$http.get(SELLER_ATTRIBUTE_ID);
        const validation = response && response.status === 200;
        !validation && new Error("cannot fetch the data");
        const result = response.data;

        this.attributeInfo = result

        const target_attribute = this.attributeInfo.filter((attribute) => 
          this.sellerInfo.seller_attribute_id === attribute.seller_attribute_id
          )
        const [ attribute ] = target_attribute
        const attributeInfo = this.attributeInfo.filter((item) => item.seller_attributes_categories_id === attribute.seller_attributes_categories_id)

        this.attributeInfo = attributeInfo

      } catch (error) {
        console.log("!!error fetch data!!")
      }
    },

    async getStatusInfo(fdata) {
      try {
        const response = await this.$http.get(SELLER_STATUS);
        const validation = response && response.status === 200;
        !validation && new Error("cannot fetch the data");
        const statusInfo = response.data;

        for (let i = 0; i < statusInfo.length; i++) {
          if (this.sellerInfo.seller_status_id === statusInfo[i].seller_status_id) {
            this.$set(this.sellerInfo, 'seller_status', statusInfo[i].name)
          }
        }

      } catch (error) {
        console.log("!!error fetch data!!")
      }
    },

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
      this.passwordModalVisible = true;
    },

    passwordChangeShowModalHandleOk(e) {
      this.loading = true;
      setTimeout(() => {
        this.passwordModalVisible = false;
        this.loading = false;
      }, 3000);
    },

    passwordChangeShowModalHandleCancel(e) {
      this.passwordModalVisible = false;
    },

    zipCodeShowModal() {
      this.zipcodeVisible = true;
    },

    handleAddress(data) {
      let fullAddress = data.address
      let extraAddress = ''
      if (data.addressType === 'R') {
        if (data.bname !== '') {
          extraAddress += data.bname
        }
        if (data.buildingName !== '') {
          extraAddress += (extraAddress !== '' ? `, ${data.buildingName}` : data.buildingName)
        }
        fullAddress += (extraAddress !== '' ? ` (${extraAddress})` : '')
      }

      console.log(fullAddress)
    },

    onClickImageUpload(info) {
      if (info.file.status === 'uploading') {
        this.loading = true;
        return;
      }
      if (info.file.status === 'done') {
        // Get this url from response in real world.
        getBase64(info.file.originFileObj, imageUrl => {
          this.profileImageUrl = imageUrl;
          this.loading = false;
        });
      }
    },

    onClickBackgroundImageUpload(info) {
      if (info.file.status === 'uploading') {
        this.loading = true;
        return;
      }
      if (info.file.status === 'done') {
        // Get this url from response in real world.
        getBase64(info.file.originFileObj, imageUrl => {
          this.backgroundImageUrl = imageUrl;
          this.loading = false;
        });
      }
    },

    beforeUpload(file) {
      const isJpgOrPng = file.type === 'image/jpeg' || file.type === 'image/png';
      if (!isJpgOrPng) {
        this.$message.error('You can only upload JPG file!');
      }
      const isLt2M = file.size / 1024 / 1024 < 5;
      if (!isLt2M) {
        this.$message.error('Image must smaller than 2MB!');
      }
      return isJpgOrPng && isLt2M;
    },
    
    onClickImageDelete() {
      this.profileImageUrl = '';
    },

    onClickBackgroundImageDelete() {
      this.backgroundImageUrl = '';
    }
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
        width: 190px;
        height: 190px;
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
  width: 200px;
  height: 200px;
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
  width: 45%;
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

.align {
  text-align: center;
  margin-bottom: 25px;
}
/* 여기다 css */
</style>

