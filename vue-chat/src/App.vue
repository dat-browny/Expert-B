<template>
    <div id="app">
        <div class="content">
            <div class="chat-container">
                <Chat v-if="visible"
                      :participants="participants"
                      :myself="myself"
                      :messages="messages"
                      :chat-title="chatTitle"
                      :placeholder="placeholder"
                      :colors="colors"
                      :border-style="borderStyle"
                      :hide-close-button="hideCloseButton"
                      :close-button-icon-size="closeButtonIconSize"
                      :submit-icon-size="submitIconSize"
                      :submit-image-icon-size="submitImageIconSize"
                      :load-more-messages="toLoad.length > 0 ? loadMoreMessages : null"
                      :async-mode="asyncMode"
                      :scroll-bottom="scrollBottom"
                      :display-header="true"
                      :send-images="false"
                      :profile-picture-config="profilePictureConfig"
                      :timestamp-config="timestampConfig"
                      :link-options="linkOptions"
                      @onMessageSubmit="onMessageSubmit"
                      @onType="onType"
                      @onClose="onClose('param value')"/>
            </div>
            
        </div>
    </div>
</template>

<script>
import axios from 'axios';
import Chat from './components/Chat.vue'

export default {
    name: 'app',
    components: {
        Chat
    },
    data() {
        return {
            visible: true,
            output : null,
            participants: [
                {
                    name: 'Smart Assistant',
                    id: 1,
                    profilePicture: require("./assets/bot.png")
                }
                
            ],
            myself: {
                name: 'Customer',
                id: 3,
                profilePicture: require("./assets/customer.png")
            },
            messages: [
                {
                    content: "Hello ! I am a Smart Assistant",
                    participantId: 1,
                    timestamp: {year: 2023, month: 3, day: 5, hour: 20, minute: 10, second: 3, millisecond: 123},
                    uploaded: true,
                    viewed: true,
                    type: 'text'
                },
                
            ],
            chatTitle: 'My chat title',
            placeholder: 'send your message',
            colors: {
                header: {
                    bg: '#d30303',
                    text: '#fff'
                },
                message: {
                    myself: {
                        bg: '#fff',
                        text: '#525252'
                    },
                    others: {
                        bg: '#fb4141',
                        text: '#fff'
                    },
                    messagesDisplay: {
                        //bg: 'rgb(247, 243, 243)',
                        //bg: '#f7f3f3'
                        bg: '#f7f3f3'
                    }
                },
                submitIcon: '#b91010',
                submitImageIcon: '#b91010',
            },
            borderStyle: {
                topLeft: "10px",
                topRight: "10px",
                bottomLeft: "10px",
                bottomRight: "10px",
            },
            hideCloseButton: true,
            submitIconSize: 24,
            submitImageIconSize: 24,
            closeButtonIconSize: "20px",
            asyncMode: true,
            toLoad: [

            ],
            scrollBottom: {
                messageSent: true,
                messageReceived: false
            },
            profilePictureConfig: {
                others: true,
                myself: true,
                styles: {
                    width: '50px',
                    height: '50px',
                    borderRadius: '50%'
                }
            },
            timestampConfig: {
                format: 'HH:mm',
                relative: false
            },
            // there are other options, you can check them here
            // https://soapbox.github.io/linkifyjs/docs/options.html
            linkOptions: {
                myself: {
                    className: 'myLinkClass',
                    events: {
                        click: function (e) {
                            alert('Link clicked!');
                        },
                        mouseover: function (e) {
                            alert('Link hovered!');
                        }
                    },
                    format: function (value, type) {
                        if (type === 'url' && value.length > 50) {
                            value = value.slice(0, 50) + '…';
                        }
                        return value;
                    }
                },
                others: {
                    className: 'othersLinkClass',
                    events: {
                        click: function (e) {
                            alert('Link clicked!');
                        },
                        mouseover: function (e) {
                            alert('Link hovered!');
                        }
                    },
                    format: function (value, type) {
                        if (type === 'url' && value.length > 50) {
                            value = value.slice(0, 50) + '…';
                        }
                        return value;
                    }
                }
            }
        }
    },
    methods: {
        // eslint-disable-next-line
        onType: function (e) {
            // eslint-disable-next-line
            console.log('typing');
        },
        loadMoreMessages(resolve) {
            setTimeout(() => {
                resolve(this.toLoad);
                this.messages.unshift(...this.toLoad);
                this.toLoad = [];
            }, 1000);
        },
        onMessageSubmit(message) {
            this.messages.push(message);
            
            axios.get(`http://127.0.0.1:3000/chat`,{params: {text: message['content']}})
            .then(response => {
            this.output = response.data['message']
            console.log(this.output)
            this.messages.push(
                {
                    type: 'text',
                    preview: null,
                    src: 'https://pbs.twimg.com/profile_images/875996174305472512/upM71pVR.jpg',
                    content: this.output,
                    participantId: 1,
                    
                    uploaded: true,
                    viewed: false
                }
            );
            
            })
            .catch(e => {
            this.errors.push(e)
            })

            setTimeout(() => {
                message.uploaded = true
                message.viewed = true
            }, 2000)
        },
        onClose(param) {
            console.log(param)
            this.visible = false;
        },
     
        onImageSelected({file, message}){
            let src = 'https://pbs.twimg.com/profile_images/875996174305472512/upM71pVR.jpg'
            this.messages.push(message);

            setTimeout((res) => {
                message.uploaded = true
                message.src = res.src
            }, 3000, {src});
        },
        onImageClicked(message){

            console.log('Image clicked', message.src)
        }
    }
}
</script>

<style>
#app {
    font-family: 'Avenir', Helvetica, Arial, sans-serif;
    -webkit-font-smoothing: antialiased;
    -moz-osx-font-smoothing: grayscale;
    text-align: center;
    color: #2c3e50;
    margin-top: 60px;
}

.content {
    width: 100%;
    display: flex;
    align-items: center;
    justify-content: space-evenly;
    flex-wrap: wrap;
}

.chat-container {
    display: flex;
    align-items: center;
    justify-content: center;
    background: rgb(247, 243, 243);
    padding: 10px 0 10px 0;
    height: 800px;
    width: 100%;
}

.external-controller {
    background: #2c3e50;
    height: 300px;
    width: 600px;
    display: flex;
    color: #eee;
}

.controller-btn-container {
    display: flex;
    justify-content: center;
    align-items: center;
    padding-left: 20px;
    padding-right: 20px;
    flex-wrap: wrap;
}

.btn-message {
    cursor: pointer;
    background: #eee;
    border: none;
    height: 40px;
    color: #2c3e50;
    border-radius: 5px;
    outline: none;
    transition: 0.3s;
}

.btn-participant {
    cursor: pointer;
    background: #eee;
    border: none;
    height: 40px;
    color: #2c3e50;
    border-radius: 5px;
    outline: none;
    transition: 0.3s;
}

.btn-message:hover {
    background: rgb(255, 255, 255);
}

</style>
