## React
#### 1. Общее
Включайте только один React компонент в файл.
Всегда используйте JSX синтаксис.
Если у вас есть внутреннее состояние (`state`) и/или ссылки (`refs`), отдавайте предпочтение `class extends React.Component`. В ином случае используйте функции.
#### 2. Именование
**Расширения**: Используйте расширение .jsx для компонентов React.
**Имя файла**: Используйте `PascalCase` для названий файлов.
```javascript
import ReservationCard from './ReservationCard';
```
**Именование переменной**: Используйте `PascalCase` для компонентов React и `camelCase` для их экземпляров.
```javascript
const reservationItem = <ReservationCard />;
```
**Именование компонента**: Называйте файлы так же как и компоненты. Корневые компоненты в директории должны лежать в файле index.jsx, и в этом случае название папки должно быть таким же, как название компонента:
```javascript
import Footer from './Footer';
```
**Выравнивание**
Следуйте приведённым ниже стилям для JSX-синтаксиса.
```javascipt
<Foo
  superLongParam="bar"
  anotherSuperLongParam="baz"
/>
```
**Кавычки**
Всегда используйте двойные кавычки (") для JSX-атрибутов, а одинарные кавычки (') для всего остального JS.
```javascript
<Foo bar="bar" />
<Foo style={{ left: '20px' }} />
```
**Пробелы**: 
Всегда вставляйте один пробел в ваш самозакрывающийся тег.
Не отделяйте фигурные скобки пробелами в JSX. eslint: react/jsx-curly-spacing
```javascript
<Foo bar={baz} />
```
**Свойства (Props)**
Всегда используйте camelCase для названий свойств.
```javascript
<Foo userName="hello" phoneNumber={12345678}/>
```
Не указывайте значение свойства, когда оно явно true.
```javascript
<Foo hidden />
```
Всегда указывайте подробные `defaultProps` для всех свойств, которые не указаны как необходимые.
```javascript
const Component = ({foo, bar}) => {
  return <div>{foo}{bar}</div>;  
}
Component.propTypes = {
  foo: PropTypes.number.isRequired,
  bar: PropTypes.string,
};
Component.defaultProps = {
  bar: '',
};
```
**Ссылки (Refs)**
Всегда используйте функции обратного вызова.
```javascript
<Foo ref={ref => { this.myRef = ref; }}/>
```
**Круглые скобки**
Оборачивайте в скобки JSX теги, когда они занимают больше одной строки.
```javascript
render() {
  return (
    <MyComponent variant="long body" foo="bar">
      <MyChild />
    </MyComponent>
  );
}
```
**Теги**
Всегда используйте самозакрывающиеся теги, если у элемента нет дочерних элементов.
```javascript
<Foo variant="stuff" />
```
Если ваш компонент имеет множество свойств, которые располагаются на нескольких строчках, то закрывайте тег на новой строке.
```javascript
<Foo
  bar="bar"
  baz="baz"
/>
```
**Методы**
Используйте стрелочные функции для замыкания локальных переменных.
```javascript
<Item
  key={item.key}
  onClick={() => doSomethingWith(item.name, index)}
/>
```
**`Не привязывайте обработчики событий в методе render`** .
Вызов bind в методе render создаёт новую функцию при каждой перерисовке.

#### 3.Последовательность
Последовательность для class extends React.Component:
* произвольные static методы
* constructor
* componentWillMount
* componentDidMount
* componentWillReceiveProps
* shouldComponentUpdate
* componentWillUpdate
* componentDidUpdate
* componentWillUnmount
* обработчики кликов или событий, такие как `onClickSubmit()`
* getter методы для render, такие как `getSelectReason()`
* произвольные render методы, такие как `renderNavigation()`
* render
#### 4. Как определять propTypes, defaultProps, и т.д.
```javascript
import React from 'react';
import Proptypes from 'prop-types';

class Link extends React.Component {
  render() {
    return <a href={this.props.url} data-id={this.props.id}>{this.props.text}</a>;
  }
}

Link.propTypes = {
  id: PropTypes.number.isRequired,
  url: PropTypes.string.isRequired,
  text: PropTypes.string,
};
Link.defaultProps = {
  text: 'Hello World',
};

export default Link;
```
