import { Suspense, useState } from 'react'
import './App.css'
import { greetingService } from './api/greetingService'

const DEFAULT_MESSAGE = 'Arriving Soon...'
function App() {
  const [greeting, setGreeting] = useState()
  const [mongoGreeting, setMongoGreeting] = useState()
  const handleGreetings = async () => {
    const { greeting } = await greetingService.getDefaultGreeting()
    const { greeting: mongoGreeting} = await greetingService.getMongoGreeting()
    setGreeting(greeting)
    setMongoGreeting(mongoGreeting)
  }
  handleGreetings();
  
  return (
    <div>
      <h1>Hello World</h1>
      <Suspense>
        <h2>Flask: {greeting} </h2>
      </Suspense>
      <Suspense>
        <h2>Mongo: {mongoGreeting}</h2>
      </Suspense>
      
    </div>
  )
}

export default App
