import React, { Component } from 'react';
import '../static/css/Chat.scss';
import WebSocketInstance from '../WebSocket';

class ChatComponent extends Component {
    constructor(props) {
        super(props)
    
        this.state = {
            message : '',
            messages : []
        }
        this.waitForSocketConnection(() => {
            WebSocketInstance.initChatUser(this.props.currentUser);
            WebSocketInstance.addCallbacks(this.setMessages.bind(this), this.addMessage.bind(this));
            WebSocketInstance.fetchMessages(this.props.currentUser);
        });
    }
    
    waitForSocketConnection(callback) {
        const component = this;
        setTimeout(
            function(){
                if(WebSocketInstance.state() === 1){
                    console.log('Connection is made');
                    callback();
                    return;
                }
                else{
                    console.log("Waiting for connection..");
                    component.waitForSocketConnection(callback);
                }
            }, 100);
    }

    scrollToBottom = () => {
        const chat = this.messagesEnd;
        const scrollHeight = chat.scrollHeight;
        const height = chat.clientHeight;
        const maxScrollTop = scrollHeight - height;
        chat.scrollTop = maxScrollTop > 0 ? maxScrollTop : 0;
    }
    addMessage(message) {
        this.setState({
            messages : [...this.state.messages, message]
        });
    }
    
    setMessages(messages){
        this.setState ({
            messages : messages.reverse()
        });
        console.log('This was called')
    }
    
    messageChangeHandler = (event) => {
        this.setState({
            message : event.target.value
        });
    }

    sendMessageHandler = (e, message) => {
        const messageObject = {
            from : this.props.currentUser,
            text : message
        };
        WebSocketInstance.newChatMessage(messageObject);
        
        this.setState({
            message : ''
        });

        e.preventDefault();
    }

    renderMessages = (messages) => {
        const currentUser = this.props.currentUser;
        return messages.map((message, i) => {
            return (
            <li key={message.id}className={message.author === currentUser ? 'me' : 'her'}
            >
                <h4 className='author'>
                    {message.author}
                </h4>
                <p>
                    {message.content}
                </p>
            </li>
            );

        });
    }

    componentDidMount() {
        this.scrollToBottom();
    }
    componentDidUpdate() {
        this.scrollToBottom();
    }

    render() {
        const messages = this.state.messages;
        const currentUser = this.props.currentUser;
        return (
            <div className='chat'>
                <div className="container">
                    <h1>Chatting as {currentUser}</h1>
                    <h3>Displaying only the recent 50 messages</h3>
                    <ul ref={(el) => {this.messagesEnd = el; }}>
                        {
                            messages && 
                            this.renderMessages(messages)
                        }
                    </ul>
                </div>
                <div className="container message-form">
                    <form 
                    onSubmit={(e) => this.sendMessageHandler(e, this.state.message)}
                    className="form">
                        <input 
                        type="text"
                        onChange={this.messageChangeHandler}
                        value={this.state.message}
                        placeholder="Start Typing"
                        required />
                        <button type="submit" className="submit" value="Submit">
                            Send
                        </button>
                    </form>
                </div>
            </div>
        );
    }
}

export default ChatComponent;