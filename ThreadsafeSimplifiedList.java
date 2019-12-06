package io.dama.par.hoh;

import java.util.concurrent.locks.ReentrantLock;


public class ThreadsafeSimplifiedList<T> implements SimplifiedList<T>{

	private Node<T> first;

	private class Node<U> {
		private U element;
		private Node<U> prev;
		private Node<U> next;
		private ReentrantLock lock; //sonst kann man nicht von außen darauf zugreifen

		private Node(final U element, final Node<U> prev, final Node<U> next) {
			super();
			this.element = element;
			this.prev = prev;
			this.next = next;
			this.lock = new ReentrantLock();
		}
	}

	public ThreadsafeSimplifiedList() {
		super();
		this.first = null;
	}

	@Override
	public T get(final int i) {
		this.first.lock.lock();
		Node<T> ptr = this.first;
		try {
			for(int j = 0; j < i; j++) {
				ptr.next.lock.lock();
				ptr = ptr.next;
				ptr.prev.lock.unlock();
			}
			return delay(ptr.element);
		} finally {
			ptr.lock.unlock();
		}
	}

	@Override
	public boolean add(final T e) {
		if(!this.isEmpty()) {
			this.first.lock.lock();
			Node<T> ptr = this.first;
			while(ptr.next != null) {
				ptr.next.lock.lock();
				ptr = ptr.next;
				ptr.prev.lock.unlock();
			}
			ptr.next = new Node<>(e, ptr, null);
		} else {
			//Es gibt kein first, das man locken könnte, das Setzen der Wurzel 
			//muss trotzdem geschützt werden
			synchronized (this) {
				this.first = new Node<>(e, null, null);
			}
		}
		return true;
	}

	@Override
	public T set(final int i, final T e) {
		first.lock.lock();
		Node<T> ptr = first;
		try {
			for(int j = 0; j < i; j++) {
				ptr.next.lock.lock();
				ptr = ptr.next;
				ptr.prev.lock.unlock();
			}
			ptr.element = e;
			return e;
		} finally {
			ptr.lock.unlock();
		}
	}

	@Override
	public boolean isEmpty() {
		synchronized (this) {
			return this.first == null;
		}

	}
}
