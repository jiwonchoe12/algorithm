import Interface_form.Queue;
import java.util.Comparator;

public class PriorityQueue<E> implements Queue<E> {
 
	private final Comparator<? super E> comparator;
	private static final int DEFAULT_CAPACITY = 10;	// 최소(기본) 용적 크기 
 
	private int size;	// 요소 개수
	private Object[] array;	// 요소를 담을 배열
 
	// 생성자 Type 1 (초기 공간 할당 X)
	public PriorityQueue() {
		this(null);
	}
	
	public PriorityQueue(Comparator<? super E> comparator) {
		this.array = new Object[DEFAULT_CAPACITY];
		this.size = 0;
		this.comparator = comparator;
	}
 
	// 생성자 Type 2 (초기 공간 할당 O)
	public PriorityQueue(int capacity) {
		this(capacity, null);
	}
	
	public PriorityQueue(int capacity, Comparator<? super E> comparator) {
		this.array = new Object[capacity];
		this.size = 0;
		this.comparator = comparator;
	}
 
	
	// 받은 인덱스의 부모 노드 인덱스를 반환
	private int getParent(int index) {
		return index / 2;
	}
	
	// 받은 인덱스의 왼쪽 자식 노드 인덱스를 반환
	private int getLeftChild(int index) {
		return index * 2;
	}
	
	// 받은 인덱스의 오른쪽 자식 노드 인덱스를 반환
	private int getRightChild(int index) {
		return index * 2 + 1;
	}

	private void resize(int newCapacity) {
		
		// 새로 만들 배열
		Object[] newArray = new Object[newCapacity];
		
		// 새 배열에 기존에 있던 배열의 요소들을 모두 복사해준다. 
		for(int i = 1; i <= size; i++) {
			newArray[i] = array[i];
		}
	
		/*
		* 현재 배열은 GC 처리를 위해 null로 명확하게 처리한 뒤
		* 새 배열을 array에 연결해준다.
		*/
		this.array = null;
		this.array = newArray;
		
	}
}