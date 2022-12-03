### Facts about Reactjs
- useRef vs createRef
	Use useRef for mutable references. CreateRef returns a readonly reference.
	
	Example:
	const isMounted = useRef<boolean>();
	
	useEffect(() => {
		if(!isMounted.current)
			isMounted.current = true;
			
		return () => {
			isMounted.current = false;
		}	
	})
	
- The order of useEffect hook matters
